graph = {
    'A': ['B', 'C','D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'G'],
    'E': [],
    'F': ['I', 'J'],
    'G': ['K'],
    'H': [],
    'K': [],
    'I': [],
    'J': ['K']
    }

def dfs (node, visited, stack):
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited, stack)
    stack.append(node)


def topological_sort(graph):
    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfs(node, visited, stack)

    return stack[ : : -1]

result = topological_sort(graph)

print("Toplogical sorting order: ", result)
    
    
