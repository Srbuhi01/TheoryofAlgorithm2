def find_connected_components(matrix):
    n = len(matrix)  # գագաթների քանակը
    visited = [False] * n
    components = []

    def dfs(node, component):
        visited[node] = True
        component.append(node)
        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor, component)

    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, component)
            components.append(component)

    return components

adj_matrix = [
    [0, 1, 1, 0, 0, 0],  # 0
    [1, 0, 1, 0, 0, 0],  # 1
    [1, 1, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 1, 0],  # 3
    [0, 0, 0, 1, 0, 0],  # 4
    [0, 0, 0, 0, 0, 0]   # 5
]

components = find_connected_components(adj_matrix)
print(components)

