graph = {
    0: [11, 7, 9],
    9: [10, 8],
    7: [11, 6, 3],
    10: [1],
    8: [1, 12],
    6: [5],
    3: [2, 4],
    12: [2],
    11: [],
    5: [],
    2: [],
    4: [],
    1: []
}

def bfs(start, end):
    queue = [start]  
    visited = set()   #for visited nodes
    visited.add(start)
    
    prev = {start: None}  

    while queue:     #while not empty pop 
        node = queue.pop(0) 
        
        if node == end:
            break  # end node
        
        for neighbor in graph.get(node, []):  #all neighbors
            if neighbor not in visited:
                queue.append(neighbor)  
                visited.add(neighbor)
                prev[neighbor] = node  # prev node

    # return path
    path = []
    current = end
    while current is not None: 
        path.append(current)
        current = prev.get(current)

    return path[::-1] if path and path[-1] == start else []  

start_node = 0
end_node = 12
print( bfs(start_node, end_node))
