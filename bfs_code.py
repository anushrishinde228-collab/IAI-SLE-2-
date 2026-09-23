# bfs_code.py
from collections import deque
from common import GRAPH, START, GOAL


def bfs(graph, start=START, goal=GOAL):
    """Breadth-First Search. Returns (path, nodes_expanded)."""
    nodes_expanded = 0
    frontier = deque([(start, [start])])
    visited = {start}

    while frontier:
        node, path = frontier.popleft()
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                frontier.append((neighbor, path + [neighbor]))

    return None, nodes_expanded


if __name__ == "__main__":
    path, nodes = bfs(GRAPH)
    print("BFS path:", path)
    print("BFS nodes expanded:", nodes)