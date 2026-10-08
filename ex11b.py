n = int(input("Enter the number of users: "))

graph = [[] for _ in range(n)]

e = int(input("Enter the number of connections: "))

print("Enter the connections (u v):")
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n):
    graph[i].sort()

start = int(input("Enter the starting user: "))

visited = [False] * n
queue = [start]
visited[start] = True
bfs = []

while queue:
    node = queue.pop(0)
    bfs.append(node)

    for neighbour in graph[node]:
        if not visited[neighbour]:
            visited[neighbour] = True
            queue.append(neighbour)

visited = [False] * n
dfs = []

def dfs_traversal(node):
    visited[node] = True
    dfs.append(node)

    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs_traversal(neighbour)

dfs_traversal(start)

print("\nBFS Traversal:")
print(*bfs)

print("\nDFS Traversal:")
print(*dfs)

print("\nReachable Users:")
print(*bfs)