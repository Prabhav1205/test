INF = float('inf')
n = int(input("Enter number of vertices: "))
c = []
print("Enter adjacency matrix (use inf for no edge):")
for i in range(n):
    row = input().split()
    row = [INF if x.lower() == "inf" else float(x) for x in row]
    c.append(row)
near = [-1] * n
t = []
mcost = 0
m = INF
for i in range(n):
    for j in range(i + 1, n):
        if c[i][j] < m:
            m, k, l = c[i][j], i, j
t.append((k, l))
mcost += m
for i in range(n):
    if i != k and i != l:
        near[i] = k if c[i][k] < c[i][l] else l
near[k] = near[l] = -1
def output(step, j):
    print(f"\nStep {step}")
    print("Selected Edges:")
    for u, v in t:
        print(f"({u + 1}, {v + 1}) -> {c[u][v]}")
    if j != -1:
        print(f"Selected Vertex (j): {j + 1}")
    print(f"Mincost: {mcost}")
    print("\nNode  :", " ".join(f"{i + 1:>4}" for i in range(n)))
    print("Near  :", " ".join(
        f"{x + 1:>4}" if x != -1 else "   -"
        for x in near
    ))
    print("Cost  :", " ".join(
        f"{c[i][near[i]]:>4}"
        if near[i] != -1 else "   -"
        for i in range(n)
    ))
output(1, -1)
for step in range(2, n):
    j = min(
        (i for i in range(n) if near[i] != -1),
        key=lambda i: c[i][near[i]]
    )
    k = near[j]
    t.append((j, k))
    mcost += c[j][k]
    near[j] = -1
    for i in range(n):
        if near[i] != -1 and c[i][j] < c[i][near[i]]:
            near[i] = j
    output(step, j)
print(f"\nFinal Minimum Cost: {mcost}")
print("\nEdges in Minimum Spanning Tree:")
for i, (u, v) in enumerate(t, 1):
    print(f"Edge {i}: ({u + 1}, {v + 1}) -> {c[u][v]}")