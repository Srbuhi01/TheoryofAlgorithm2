def validPath(n, edges, source, destination):

    # adjacency list
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    #  DFS to check if a path exists
    def dfs(node, visited):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                if dfs(neighbor, visited):
                    return True
        return False

    # Start DFS
    visited = set()
    return dfs(source, visited)

n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

print(validPath(n, edges, source, destination))
