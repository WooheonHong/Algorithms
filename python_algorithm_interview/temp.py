from typing import List
from collections import deque

graph_list = {
    1: set([2, 3, 4]),
    2: set([5]),
    3: set([5]),
    4: set([]),
    5: set([6, 7]),
    6: set([]),
    7: set([3]),
}
root_node = 1


def dfs_recursive(v, visited: List):
    visited.append(v)
    for w in graph_list[v]:
        if w not in visited:
            visited = dfs_recursive(w, visited)

    return visited
