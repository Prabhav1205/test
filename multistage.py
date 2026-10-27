INF = float('inf')
def FGraph(Gr, k, n, p):
    cost = [INF] * (n + 1)
    d = [0] * (n + 1)
    cost[n] = 0
    print("\n========== FORWARD APPROACH ==========")
    for j in range(n - 1, 0, -1):
        candidates = []
        for r in range(1, n + 1):
            if Gr[j][r] != INF:
                candidates.append((Gr[j][r] + cost[r], r))
        if candidates:
            values = [v for v, r in candidates]
            minimum, vertex = min(candidates)
            print(f"cost[{j}] = min({', '.join(f'{v:g}' for v in values)}) = {minimum:g}")
            cost[j] = minimum
            d[j] = vertex
            print(f"d[{j}] = {d[j]}")
    p[1] = 1
    p[k] = n
    for j in range(2, k):
        p[j] = d[p[j - 1]]
    print("\nMinimum-cost path:")
    print(" -> ".join(str(p[j]) for j in range(1, k + 1)))
    print("Minimum cost =", cost[1])
    return cost, d, p
def BGraph(Gr, k, n, p):
    bcost = [INF] * (n + 1)
    d = [0] * (n + 1)
    bcost[1] = 0
    print("\n========== BACKWARD APPROACH ==========")
    for j in range(2, n + 1):
        candidates = []
        for r in range(1, j):
            if Gr[r][j] != INF and bcost[r] != INF:
                candidates.append((bcost[r] + Gr[r][j], r))
        if candidates:
            values = [v for v, r in candidates]
            minimum, vertex = min(candidates)
            print(f"bcost[{j}] = min({', '.join(f'{v:g}' for v in values)}) = {minimum:g}")
            bcost[j] = minimum
            d[j] = vertex
            print(f"d[{j}] = {d[j]}")
    p[1] = 1
    p[k] = n
    for j in range(k - 1, 1, -1):
        p[j] = d[p[j + 1]]
    print("\nMinimum-cost path:")
    print(" -> ".join(str(p[j]) for j in range(1, k + 1)))
    print("Minimum cost =", bcost[n])
    return bcost, d, p
n = 16
k = 6
M = [
    [INF, 11, 8, 1, 13, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, 10, 7, 8, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, 9, INF, 12, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, 15, 5, 6, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, 7, 1, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 9, 9, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 11, 4, 13, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, 13, INF, INF, 8, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 15, 14, 4, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 15, 2, 8, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 13, 3, 8, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 9, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 4],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 12],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 12],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]
]
Gr = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        Gr[i + 1][j + 1] = M[i][j]
p = [0] * (k + 1)
cost, d, p = FGraph(Gr, k, n, p)
p = [0] * (k + 1)
bcost, d, p = BGraph(Gr, k, n, p)