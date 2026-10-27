INF = float('inf')
cost = [
    [0,   35, 25, 20, 31, 28, INF, 20],
    [INF, 0,  30, INF, 15, 35, INF, INF],
    [33,  27, 0,  24, 23, 21, 17, 12],
    [27,  10, 20, 0,  INF, INF, 26, INF],
    [INF, 13, INF, 18, 0,  INF, 17, 21],
    [30,  32, INF, 31, INF, 0,  20, INF],
    [19,  INF, INF, 35, 17, 15, 0,  INF],
    [INF, INF, 35, 29, 30, INF, INF, 0]
]
n = 8
source = 0
s = [False] * n
dist = [INF] * n
p = [-1] * n
for i in range(n):
    dist[i] = cost[source][i]
    if cost[source][i] != INF:
        p[i] = source
dist[source] = 0
s[source] = True
p[source] = -1
print("Dijkstra's Algorithm")
print()
print("Step 1 : v = 1")
print("s    =", s)
print("p    =", [x + 1 if x != -1 else -1 for x in p])
print("dist =", dist)
print()
for step in range(2, n + 1):
    v = -1
    minimum = INF
    for i in range(n):
        if not s[i] and dist[i] < minimum:
            minimum = dist[i]
            v = i
    s[v] = True
    for w in range(n):
        if not s[w] and cost[v][w] != INF:
            if dist[w] > dist[v] + cost[v][w]:
                dist[w] = dist[v] + cost[v][w]
                p[w] = v
    print("Step", step, ": u =", v + 1)
    print("s    =", s)
    print("p    =", [x + 1 if x != -1 else -1 for x in p])
    print("dist =", dist)
    print()
def get_path(destination):
    path = []
    current = destination
    while current != -1:
        path.append(current + 1)
        current = p[current]
    path.reverse()
    return " -> ".join(map(str, path))
print("--------------------------------------------")
print("Src\tDest\tLength\tPath")
print("--------------------------------------------")
for i in range(1, n):
    print(f"1\t{i + 1}\t{int(dist[i])}\t{get_path(i)}")