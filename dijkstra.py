inf = 999999
n = 5
graph = [
    [0, 3, 5, inf, inf],
    [inf, 0, 2, 6, inf],
    [inf, 1, 0, 4, 6],
    [inf, inf, inf, 0, 2],
    [3, inf, inf, inf, 0]
]

start = 0
distance = [inf] * n
visited = [False] * n

distance[start] = 0

for _ in range(n):
    min_val = inf
    curr = -1
    for i in range(n):
        if not visited[i] and distance[i] < min_val:
            min_val = distance[i]
            curr = i
            
    if curr == -1:
        break
        
    visited[curr] = True
    
    for next_node in range(n):
        cost = graph[curr][next_node]
        if cost != inf:
            if distance[curr] + cost < distance[next_node]:
                distance[next_node] = distance[curr] + cost

print(distance)
