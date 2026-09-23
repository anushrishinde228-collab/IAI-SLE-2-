# run_bfs.py
import timeit
from common import GRAPH
from bfs_code import bfs


def main():
    NUMBER = 10_000
    REPEAT = 5

    timer = timeit.Timer(stmt="bfs(GRAPH)", globals=globals())
    results = timer.repeat(repeat=REPEAT, number=NUMBER)

    per_run_ms = [(t / NUMBER) * 1000 for t in results]
    best_ms = min(per_run_ms)
    avg_ms = sum(per_run_ms) / len(per_run_ms)

    path, nodes = bfs(GRAPH)

    print("=== BFS Benchmark ===")
    print(f"Runs per measurement : {NUMBER}")
    print(f"Repeats              : {REPEAT}")
    print(f"Per-run times (ms)   : {[round(x, 5) for x in per_run_ms]}")
    print(f"Best  (ms)           : {best_ms:.5f}")
    print(f"Average (ms)         : {avg_ms:.5f}")
    print(f"Nodes expanded       : {nodes}")
    print(f"Path found           : {path}")


if __name__ == "__main__":
    main()