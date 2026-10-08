n = int(input("Enter number of cities: "))
print("Enter the adjacency matrix:")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
src = int(input("Enter source city: "))
dest = int(input("Enter destination city: "))
INF = 999999
dist = [INF] * n
visited = [False] * n
parent = [-1] * n
dist[src] = 0
for _ in range(n):
    u = -1
    for i in range(n):
        if not visited[i] and (u == -1 or dist[i] < dist[u]):
            u = i
        if u == -1:
            break
    visited[u] = True
    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u
path = []
v = dest
while v != -1:
    path.append(v)
    v = parent[v]
path.reverse()
if dist[dest] == INF:
    print("No path exists")
else:
    print("Shortest path:", " -> ".join(map(str, path)))
    print("Distance:", dist[dest])