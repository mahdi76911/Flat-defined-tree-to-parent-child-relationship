# Flat-Defined Tree → Parent/Child Relationship

Given a tree where every node's name is a dotted hierarchy path
(`a.b.c` means `c` is a child of `b`, which is a child of `a`), derive the
explicit **parent / child** relationship as a flat table.

## Idea
The path itself encodes the hierarchy. For a node `x.y.z` (id 5):
- `z` (id 5) is a child of `y`
- `y` (id 4) is a child of `x`
- `x` (id 3) is a child of `root`

So each node (except the root) produces one parent→child edge, and the root
sits at the top with no parent.

## Input
A text file, one path per line (empty lines ignored):
```
root
root.a
root.a.b
root.c
root.c.d
```

## Output
A flat list of edges — `[parent, child, parent_id, child_id]` — using stable
ids (root = 0, every other path gets the next id in input order):
```
[root, a, 0, 3]
[a, b, 3, 4]
[root, c, 0, 6]
[c, d, 6, 7]
```
A node with **no children** (e.g. `b`) simply has no outgoing edge — the
parent→child list captures the whole tree.

## Run

### CLI
```bash
python main.py <input.txt>
```
Writes the edge list to the console.

### GUI
```bash
python gui.py
```
Pick the input file, run it, and read the result in the window.

## Files
| File | Purpose |
|------|---------|
| `main.py` | CLI: parse dotted paths → parent/child edges |
| `gui.py` | tkinter UI over the same logic |
| `Info.txt` | Original task description |
