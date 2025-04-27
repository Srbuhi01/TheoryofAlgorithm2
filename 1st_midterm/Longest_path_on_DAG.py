V = 6

graph = {
    0: [(1, 5), (2, 3)],
    1: [(2, 2), (3, 6)],
    2: [(3, 7), (4, 4), (5, 2)],
    3: [(4, -1), (5, 1)],
    4: [(5, -2)],
    5: []
}

def topological_sort_util(v, visited, stack):
    visited[v] = True
    for neighbor, weight in graph.get(v, []):
        if not visited[neighbor]:
            topological_sort_util(neighbor, visited, stack)
    stack.append(v)

def longest_path(start):
    visited = [False] * V
    stack = []

    for i in range(V):
        if not visited[i]:
            topological_sort_util(i, visited, stack)

    dist = [-float('inf')] * V
    dist[start] = 0

    while stack:
        u = stack.pop()
        for v, weight in graph.get(u, []):
            if dist[u] != -float('inf') and dist[u] + weight > dist[v]:
                dist[v] = dist[u] + weight

    return dist

start_node = 1
longest_distances = longest_path(start_node)
print("Longest path from ", start_node, ":", longest_distances)
