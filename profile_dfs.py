# profile_dfs.py
from common import GRAPH, START, GOAL
from dfs_code import dfs

for _ in range(100_000):
    dfs(GRAPH, START, GOAL)