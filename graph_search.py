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


def dfs_recursive(v, visited=[]):
    visited.append(v)
    for w in graph_list[v]:
        if w not in visited:
            visited = dfs_recursive(w, visited)

    return visited


def dfs_iterative(root_node):
    visited = []
    stack = [root_node]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack += graph_list[v] - set(visited)

    return visited


def bfs_deque(root_node):
    visited = []
    queue = deque([root_node])

    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            queue += graph_list[v] - set(visited)

    return visited


print(dfs_recursive(root_node))
print(dfs_iterative(root_node))
print(bfs_deque(root_node))