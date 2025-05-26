def findRedundantConnection(edges):
    parent = [i for i in range(len(edges) + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
            return False  
        parent[rootY] = rootX
        return True

    for a, b in edges:
        if not union(a, b):
            return [a, b]


print(findRedundantConnection([[1,2],[1,3],[2,3]]))  
print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])) 
