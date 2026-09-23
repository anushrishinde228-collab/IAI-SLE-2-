# dfs_code.py
from common import GRAPH, START, GOAL


def dfs(graph, start=START, goal=GOAL):
    """
    Depth-First Search (iterative).
    Returns (path, nodes_expanded).

    Time Complexity:
        Best    : O(1)        -> start == goal
        Average : O(V + E)    -> goal found on a short deep branch
        Worst   : O(V + E)    -> goal unreachable or on last branch
    Space Complexity: O(V)    -> stack + visited
    """
    nodes_expanded = 0

    if start == goal:
        return [start], nodes_expanded

    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        if node in visited:
            continue
        visited.add(node)

        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_expanded


if __name__ == "__main__":
    path, nodes = dfs(GRAPH)
    print("DFS path:", path)
    print("DFS nodes expanded:", nodes)

