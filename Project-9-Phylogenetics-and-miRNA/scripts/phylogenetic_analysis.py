#!/usr/bin/env python3
"""Reproduce the TPI alignment, UPGMA tree, and maximum-parsimony tree."""
from pathlib import Path
from copy import deepcopy
import csv
import itertools
import math
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESULTS = ROOT / "results"


def read_fasta(path):
    records, name, parts = {}, None, []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if name is not None:
                records[name] = "".join(parts)
            name, parts = line[1:].split()[0], []
        else:
            parts.append(line.strip())
    if name is not None:
        records[name] = "".join(parts)
    return records


def nw(a, b, match=2, mismatch=-1, gap=-2):
    """Needleman-Wunsch global pairwise alignment."""
    n, m = len(a), len(b)
    score = np.zeros((n + 1, m + 1), dtype=np.int32)
    trace = np.zeros((n + 1, m + 1), dtype=np.int8)
    score[:, 0] = np.arange(n + 1) * gap
    score[0, :] = np.arange(m + 1) * gap
    trace[1:, 0], trace[0, 1:] = 1, 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            options = (score[i-1, j-1] + (match if a[i-1] == b[j-1] else mismatch),
                       score[i-1, j] + gap, score[i, j-1] + gap)
            trace[i, j] = int(np.argmax(options))
            score[i, j] = options[trace[i, j]]
    aa, bb, i, j = [], [], n, m
    while i or j:
        t = trace[i, j]
        if t == 0:
            aa.append(a[i-1]); bb.append(b[j-1]); i -= 1; j -= 1
        elif t == 1:
            aa.append(a[i-1]); bb.append("-"); i -= 1
        else:
            aa.append("-"); bb.append(b[j-1]); j -= 1
    return "".join(reversed(aa)), "".join(reversed(bb))


def reference_guided_msa(records, reference_name="Homo_sapiens"):
    """Align each homolog to a shared reference and reconcile insertion columns."""
    ref = records[reference_name]
    pairwise = {}
    max_insert = [0] * (len(ref) + 1)
    for name, seq in records.items():
        ar, asq = nw(ref, seq)
        inserts = [""] * (len(ref) + 1)
        residues = ["-"] * len(ref)
        pos = 0
        for r, s in zip(ar, asq):
            if r == "-":
                inserts[pos] += s
            else:
                residues[pos] = s
                pos += 1
        pairwise[name] = (inserts, residues)
        max_insert = [max(x, len(y)) for x, y in zip(max_insert, inserts)]
    aligned = {}
    for name, (ins, residues) in pairwise.items():
        out = []
        for pos in range(len(ref)):
            out.append(ins[pos] + "-" * (max_insert[pos] - len(ins[pos])))
            out.append(residues[pos])
        out.append(ins[-1] + "-" * (max_insert[-1] - len(ins[-1])))
        aligned[name] = "".join(out)
    return aligned


def p_distance(a, b):
    pairs = [(x, y) for x, y in zip(a, b) if x != "-" and y != "-"]
    return sum(x != y for x, y in pairs) / len(pairs)


def upgma(names, matrix):
    clusters = {i: {"members": [i], "height": 0.0, "left": None, "right": None} for i in range(len(names))}
    dist = {(i, j): matrix[i, j] for i in clusters for j in clusters if i < j}
    next_id = len(names)
    while len(clusters) > 1:
        i, j = min(dist, key=dist.get)
        if i not in clusters or j not in clusters:
            dist.pop((i, j)); continue
        d = dist[(i, j)]
        new = {"members": clusters[i]["members"] + clusters[j]["members"], "height": d / 2,
               "left": clusters[i], "right": clusters[j]}
        old_i, old_j = clusters.pop(i), clusters.pop(j)
        for k, ck in list(clusters.items()):
            vals = [matrix[a, b] for a in new["members"] for b in ck["members"]]
            dist[tuple(sorted((next_id, k)))] = float(np.mean(vals))
        clusters[next_id] = new
        next_id += 1
        dist = {k: v for k, v in dist.items() if i not in k and j not in k}
    return next(iter(clusters.values()))


def upgma_newick(node, names, parent_height=None):
    if node["left"] is None:
        label = names[node["members"][0]]
        length = 0 if parent_height is None else parent_height - node["height"]
        return f"{label}:{length:.6f}"
    inside = ",".join(upgma_newick(ch, names, node["height"]) for ch in (node["left"], node["right"]))
    if parent_height is None:
        return f"({inside});"
    return f"({inside}):{parent_height-node['height']:.6f}"


def edges(adj):
    return [(a, b) for a in adj for b in adj[a] if a < b]


def all_unrooted_binary_trees(n):
    trees = [{0: {n}, 1: {n}, 2: {n}, n: {0, 1, 2}}]
    for leaf in range(3, n):
        expanded = []
        for adj in trees:
            for a, b in edges(adj):
                t = deepcopy(adj)
                t[a].remove(b); t[b].remove(a)
                x = max(t) + 1
                t[x] = {a, b, leaf}; t[a].add(x); t[b].add(x); t[leaf] = {x}
                expanded.append(t)
        trees = expanded
    return trees


def fitch_score(adj, states_by_leaf):
    root = next(x for x in adj if len(adj[x]) > 1)
    score = 0
    def visit(node, parent):
        nonlocal score
        children = [x for x in adj[node] if x != parent]
        if not children:
            return set(states_by_leaf[node])
        current = visit(children[0], node)
        for child in children[1:]:
            other = visit(child, node)
            inter = current & other
            if inter:
                current = inter
            else:
                current = current | other; score += 1
        return current
    visit(root, None)
    return score


def parsimony_tree(aligned, names):
    columns = []
    for col in zip(*(aligned[n] for n in names)):
        if len(set(col) - {"-"}) > 1:
            columns.append([{c} if c != "-" else set("ACDEFGHIKLMNPQRSTVWY") for c in col])
    best, best_score = None, math.inf
    for adj in all_unrooted_binary_trees(len(names)):
        score = sum(fitch_score(adj, states) for states in columns)
        if score < best_score:
            best, best_score = adj, score
    return best, best_score, len(columns)


def adjacency_newick(adj, names):
    root = next(x for x in adj if len(adj[x]) > 1)
    def rec(node, parent):
        if node < len(names): return names[node]
        return "(" + ",".join(rec(x, node) for x in sorted(adj[node]) if x != parent) + ")"
    return rec(root, None) + ";"


def plot_upgma(node, names, path):
    order = []
    def leaves(x):
        if x["left"] is None: order.append(x["members"][0])
        else: leaves(x["left"]); leaves(x["right"])
    leaves(node); ypos = {leaf: i for i, leaf in enumerate(order)}
    fig, ax = plt.subplots(figsize=(9, 5.5))
    def draw(x):
        if x["left"] is None: return 0.0, ypos[x["members"][0]]
        x1, y1 = draw(x["left"]); x2, y2 = draw(x["right"]); xx = x["height"]
        ax.plot([x1, xx], [y1, y1], color="#2563eb", lw=1.8)
        ax.plot([x2, xx], [y2, y2], color="#2563eb", lw=1.8)
        ax.plot([xx, xx], [y1, y2], color="#2563eb", lw=1.8)
        return xx, (y1 + y2) / 2
    draw(node)
    xmax = node["height"]
    for leaf in order: ax.text(-0.01*xmax, ypos[leaf], names[leaf], ha="right", va="center", fontsize=10)
    ax.invert_xaxis(); ax.set_yticks([]); ax.set_xlabel("Mean amino-acid p-distance"); ax.set_title("TPI phylogeny - UPGMA")
    ax.spines[["top", "right", "left"]].set_visible(False); fig.tight_layout(); fig.savefig(path, dpi=220); plt.close(fig)


def plot_parsimony(adj, names, path, score):
    root = next(x for x in adj if len(adj[x]) > 1)
    children = {}
    def orient(node, parent):
        children[node] = [x for x in sorted(adj[node]) if x != parent]
        for x in children[node]: orient(x, node)
    orient(root, None)
    leaves = []
    def collect(node):
        if node < len(names): leaves.append(node)
        else:
            for x in children[node]: collect(x)
    collect(root); y = {leaf: i for i, leaf in enumerate(leaves)}
    fig, ax = plt.subplots(figsize=(9, 5.5))
    def draw(node, depth):
        if node < len(names): return y[node]
        ys = [draw(ch, depth+1) for ch in children[node]]; yy = sum(ys)/len(ys)
        ax.plot([depth, depth], [min(ys), max(ys)], color="#7c3aed", lw=1.8)
        for ch, cy in zip(children[node], ys): ax.plot([depth, depth+1], [cy, cy], color="#7c3aed", lw=1.8)
        return yy
    draw(root, 0)
    maxdepth = max(4, len(names)-2)
    for leaf in leaves: ax.text(maxdepth+0.15, y[leaf], names[leaf], va="center", fontsize=10)
    ax.set_xlim(-0.2, maxdepth+2.6); ax.set_yticks([]); ax.set_xticks([])
    ax.set_title(f"TPI phylogeny - maximum parsimony (score={score})")
    ax.spines[:].set_visible(False); fig.tight_layout(); fig.savefig(path, dpi=220); plt.close(fig)


def main():
    RESULTS.mkdir(exist_ok=True)
    records = read_fasta(DATA / "TPI_sequences.fasta")
    names = list(records)
    aligned = reference_guided_msa(records)
    with (RESULTS / "TPI_alignment.fasta").open("w") as f:
        for name in names:
            f.write(f">{name}\n")
            for i in range(0, len(aligned[name]), 80): f.write(aligned[name][i:i+80] + "\n")
    matrix = np.zeros((len(names), len(names)))
    for i, j in itertools.combinations(range(len(names)), 2): matrix[i,j] = matrix[j,i] = p_distance(aligned[names[i]], aligned[names[j]])
    with (RESULTS / "TPI_pairwise_distances.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["organism"] + names)
        for name, row in zip(names, matrix): w.writerow([name] + [f"{x:.6f}" for x in row])
    u = upgma(names, matrix); (RESULTS / "TPI_UPGMA_tree.nwk").write_text(upgma_newick(u, names) + "\n")
    plot_upgma(u, names, RESULTS / "TPI_UPGMA_tree.png")
    mp, score, informative = parsimony_tree(aligned, names)
    (RESULTS / "TPI_parsimony_tree.nwk").write_text(adjacency_newick(mp, names) + "\n")
    plot_parsimony(mp, names, RESULTS / "TPI_parsimony_tree.png", score)
    (RESULTS / "phylogeny_summary.txt").write_text(
        f"Sequences: {len(names)}\nAlignment length: {len(next(iter(aligned.values())))} aa\n"
        f"Parsimony-variable columns evaluated: {informative}\nBest parsimony score: {score}\n")


if __name__ == "__main__": main()
