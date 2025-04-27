def dijkstra(graph, n, start):
    visited = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]      # priority queue

    while pq:
        pq.sort()  
        minValue, index = pq.pop(0)

        if visited[index]:
            continue
        visited[index] = True

        for edge in graph[index]:
            if visited[edge['to']]:
                continue
            newDist = dist[index] + edge['cost']
            if newDist < dist[edge['to']]:
                dist[edge['to']] = newDist
                pq.append((newDist, edge['to']))

    return dist

# Define graph based on the image
graph = {
    0: [{'to': 1, 'cost': 4}, {'to': 2, 'cost': 1}],
    1: [{'to': 3, 'cost': 1}],
    2: [{'to': 1, 'cost': 2}, {'to': 3, 'cost': 5}],
    3: [{'to': 4, 'cost': 3}],
    4: []  
}

n = 5        # Number of nodes
start = 0

print(dijkstra(graph, n, start))
