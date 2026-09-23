# profile_bfs.py
from common import GRAPH, START, GOAL
from bfs_code import bfs

for _ in range(100_000):
    bfs(GRAPH, START, GOAL)