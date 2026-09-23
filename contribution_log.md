---

# Appendix A. Contribution Log

| # | File | Scope | AI contribution | Student modification |
|---|------|-------|-----------------|----------------------|
| 1 | common.py | Graph + constants | Suggested a 7-node directed graph with adjacency list and START/GOAL constants. | Verified graph; chose Start='A', Goal='G' (avg), Goal='Z' (worst). |
| 2 | bfs_code.py | Search and profiling | Suggested BFS with `deque`, `visited` set, and `nodes_expanded` counter. | Tested; verified 7 nodes expanded (avg case) and path A→C→F→G. |
| 3 | dfs_code.py | Search and profiling | Suggested DFS with `list` stack, `visited` set, and `nodes_expanded` counter. | Tested; verified 5 nodes expanded (avg case) and path A→B→E→G. |
| 4 | best_case_bfs.py | Timing | Suggested `timeit.Timer` structure with number=10000, repeat=5. | Ran 3 times; mean best ≈ 0.00048 ms; 0 nodes expanded. |
| 5 | best_case_dfs.py | Timing | Suggested equivalent `timeit.Timer` structure for DFS. | Ran 3 times; mean best ≈ 0.00047 ms; 0 nodes expanded. |
| 6 | run_bfs.py | Timing | Suggested average-case benchmark on Goal='G'. | Ran 3 times; best ≈ 0.00788 ms, avg ≈ 0.00803 ms; 7 nodes. |
| 7 | run_dfs.py | Timing | Suggested equivalent average-case benchmark on Goal='G'. | Ran 3 times; best ≈ 0.00655 ms, avg ≈ 0.00663 ms; 5 nodes. |
| 8 | worst_case_bfs.py | Timing | Suggested worst-case benchmark with unreachable Goal='Z'. | Ran 3 times; best ≈ 0.00842 ms; 7 nodes (matches O(V+E)). |
| 9 | worst_case_dfs.py | Timing | Suggested equivalent worst-case benchmark with Goal='Z'. | Ran 3 times; best ≈ 0.00756 ms; 7 nodes (matches O(V+E)). |
| 10 | profile_bfs.py | All lines | Suggested 1,000,000-iteration loop for py-spy sampling. | Ran under `py-spy record --rate 1000`; got BFS flame graph. |
| 11 | profile_dfs.py | All lines | Suggested 1,000,000-iteration loop for py-spy sampling. | Ran under `py-spy record --rate 1000`; got DFS flame graph. |
| 12 | profile_bfs.svg | Generated | Explained py-spy command + flame graph reading. | Generated; identified `deque.popleft` / `deque.append` as hot spots. |
| 13 | profile_dfs.svg | Generated | Explained py-spy command + flame graph reading. | Generated; identified `list.pop` / `list.append` as hot spots. |
| 14 | README.md | Documentation | Suggested README structure (objective, graph, complexity, results). | Filled in measured numbers, added flame graph section, wrote conclusion. |
| 15 | .gitignore | 3 lines | Suggested exclusions for `__pycache__/`, `.vscode/`, `*.pyc`. | Created to keep the repository clean. |
