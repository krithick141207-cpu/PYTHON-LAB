n = int(input("Enter the total number of users: "))

matrix = [[0 for _ in range(n)] for _ in range(n)]

e = int(input("Enter the number of connections: "))

print("Enter the connections (u v):")
for i in range(e):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

adj_list = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            adj_list[i].append(j)

print("\nAdjacency Matrix:")
for row in matrix:
    print(*row)

print("\nAdjacency List:")
for i in range(n):
    print(i, "->", adj_list[i])

u = int(input("\nEnter first user: "))
v = int(input("Enter second user: "))

if matrix[u][v] == 1:
    print("Adjacency Matrix: Users are directly connected.")
else:
    print("Adjacency Matrix: Users are not directly connected.")

if v in adj_list[u]:
    print("Adjacency List: Users are directly connected.")
else:
    print("Adjacency List: Users are not directly connected.")
