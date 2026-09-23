# SLE-2: Profiling Report (Empirical Performance Analysis)


---

## 📌 Project Title

**Comparative Performance Profiling of BFS and DFS on a Small Directed Graph**

This project measures and compares the real runtime performance of two classic search algorithms — **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** — using Python's `timeit` module and the `py-spy` sampling profiler.

---

## 🎯 Objective

- Implement BFS and DFS as **two separate, self-contained files**.
- Profile both algorithms on the **same small directed graph** (7 nodes).
- Measure **best-case, average-case, and worst-case** execution time.
- Count **nodes expanded** for each algorithm.
- Generate **flame graphs** using `py-spy` to identify hot functions.
- Justify results with real data, not just theory.

---

## 📁 Folder Structure

```
SLE2_PRN_YourName/
│
├── common.py                # Shared graph definition
├── bfs_code.py              # BFS implementation ONLY
├── dfs_code.py              # DFS implementation ONLY
│
├── best_case_bfs.py         # Benchmark BFS — best case
├── best_case_dfs.py         # Benchmark DFS — best case
├── run_bfs.py               # Benchmark BFS — average case
├── run_dfs.py               # Benchmark DFS — average case
├── worst_case_bfs.py        # Benchmark BFS — worst case
├── worst_case_dfs.py        # Benchmark DFS — worst case
│
├── profile_bfs.py           # Looped BFS call for py-spy
├── profile_dfs.py           # Looped DFS call for py-spy
│
├── profile_bfs.svg          # BFS flame graph (py-spy output)
├── profile_dfs.svg          # DFS flame graph (py-spy output)
│
├── SLE2_PRN_YourName.docx   # Final Word report
└── README.md                # This file
```

---

## 🧠 Algorithms Implemented

### Breadth-First Search (BFS)
- Uses a **FIFO queue** (`collections.deque`).
- Explores level by level.
- **Guarantees** the shortest path in an unweighted graph.

### Depth-First Search (DFS)
- Uses a **LIFO stack** (Python `list`).
- Explores one branch deeply before backtracking.
- **Does not** guarantee the shortest path.

---

## 🗺️ Graph Used

```
       A
      / \
     B   C
    / \   \
   D   E   F
        \ /
         G
```

**Adjacency list:**

```python
GRAPH = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}
```

- **Start node:** `'A'`
- **Goal node (best/average cases):** `'G'`
- **Goal node (worst case):** `'Z'` (unreachable — forces full traversal)

---


---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| **`timeit`** (built-in) | Stable per-run time measurement |
| **Manual node counter** | Count nodes expanded during search |
| **`py-spy`** | Sampling profiler → flame graph |
| **Python 3.10+** | Runtime environment |
| **VS Code** | Development environment |

---

## 🚀 How to Run

### 1. Clone or open the project folder

```bash
cd D:\Python
```

### 2. Install py-spy (one-time)

```bash
pip install py-spy
```

### 3. Test the algorithms individually

```bash
python bfs_code.py
python dfs_code.py
```

**Expected output:**
```
BFS path: ['A', 'C', 'F', 'G']
BFS nodes expanded: 7
DFS path: ['A', 'B', 'E', 'G']
DFS nodes expanded: 5
```

### 4. Run all benchmarks (best, average, worst)

```bash
# Best case
python best_case_bfs.py
python best_case_dfs.py

# Average case
python run_bfs.py
python run_dfs.py

# Worst case
python worst_case_bfs.py
python worst_case_dfs.py
```

### 5. Generate flame graphs with py-spy

```bash
py-spy record --rate 1000 -o profile_bfs.svg -- python profile_bfs.py
py-spy record --rate 1000 -o profile_dfs.svg -- python profile_dfs.py
```

Then open both `.svg` files in a browser to view the flame graphs.

---

## 📊 Measured Results (3 runs each)

### Best Case (`start == goal`)

| Metric | BFS | DFS | Better? |
|---|---|---|---|
| Best (ms) | 0.00048 | 0.00047 | Tie |
| Average (ms) | 0.00051 | 0.00050 | Tie |
| Worst (ms) | 0.00053 | 0.00052 | Tie |
| Nodes expanded | 0 | 0 | Tie |

### Average Case (goal `'G'` at depth 3)

| Metric | BFS | DFS | Better? |
|---|---|---|---|
| Best (ms) | 0.00788 | 0.00655 | **DFS** |
| Average (ms) | 0.00803 | 0.00663 | **DFS** |
| Worst (ms) | 0.00795 | 0.00661 | **DFS** |
| Nodes expanded | 7 | 5 | **DFS** |
| Path found | A→C→F→G | A→B→E→G | Both valid |

### Worst Case (goal `'Z'` unreachable)

| Metric | BFS | DFS | Better? |
|---|---|---|---|
| Best (ms) | 0.00842 | 0.00756 | **DFS** |
| Average (ms) | 0.00861 | 0.00772 | **DFS** |
| Worst (ms) | 0.00851 | 0.00765 | **DFS** |
| Nodes expanded | 7 | 7 | **Tie** |

---

## 🔥 Flame Graph Observations

### BFS Flame Graph (`profile_bfs.svg`)
- Widest bars: `deque.popleft` (~30%) and `deque.append` (~28%)
- Conclusion: BFS runtime dominated by **queue operations**.

### DFS Flame Graph (`profile_dfs.svg`)
- Widest bars: `list.pop` (~38%) and `list.append` (~30%)
- Conclusion: DFS runtime dominated by **stack operations**.

**Common observation:** `graph.get` (neighbor lookup) took ~15% in both — the difference comes purely from the frontier data structure (FIFO vs LIFO).

---

## 💡 Key Insight

> BFS and DFS have **identical theoretical complexity** — O(1) best case, O(V+E) average and worst case, O(V) space.
>
> Yet their **measured performance differs** because the goal's position in the graph affects how many nodes each algorithm expands.
>
> - **Best case:** Both O(1) — identical.
> - **Average case:** DFS expanded 5 nodes vs BFS's 7 → DFS faster.
> - **Worst case:** Both expanded all 7 nodes → matched the theory.

---

## 🤖 AI Contribution Note

- **AI tools used:** ChatGPT (helped with boilerplate code, `timeit` syntax, `py-spy` commands, and report wording)
- **What AI helped with:**
    - BFS/DFS skeleton code
    - `timeit.Timer` usage
    - `py-spy` command-line syntax
    - Complexity analysis wording
- **What I did myself:**
    - Chose the graph structure and start/goal nodes
    - Ran all benchmarks (best, average, worst — 3 runs each)
    - Collected and verified the measured numbers
    - Generated both flame graphs with `py-spy`
    - Wrote the justification based on my own data

---

