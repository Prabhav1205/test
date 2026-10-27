INF = float('inf')
def display_matrix(A, P, n, k):
    print(f"\nA^{k:<{7 * (n + 1) - 4}}       P^{k}")
    print("     ", end="")
    for j in range(n):
        print(f"{j + 1:>7}", end="")
    print("       ", end="")
    print("     ", end="")
    for j in range(n):
        print(f"{j + 1:>7}", end="")
    print()
    for i in range(n):
        print(f"{i + 1:>3}  ", end="")
        for j in range(n):
            if A[i][j] == INF:
                print(f"{'inf':>7}", end="")
            else:
                print(f"{A[i][j]:>7g}", end="")
        print("       ", end="")
        print(f"{i + 1:>3}  ", end="")
        for j in range(n):
            if P[i][j] == -1:
                print(f"{'-':>7}", end="")
            else:
                print(f"{P[i][j] + 1:>7}", end="")
        print()
def get_path(P, src, dest):
    if P[src][dest] == -1:
        return []
    path = []
    current = dest
    while current != src:
        path.append(current)
        current = P[src][current]
        if current == -1:
            return []
    path.append(src)
    path.reverse()
    return path
def AllPairsSP(cost, A, n):
    for i in range(n):
        for j in range(n):
            A[i][j] = cost[i][j]
    P = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                P[i][j] = i
    display_matrix(A, P, n, 0)
    for k in range(n):
        newA = [row[:] for row in A]
        newP = [row[:] for row in P]
        for i in range(n):
            for j in range(n):
                if A[i][k] != INF and A[k][j] != INF:
                    if A[i][j] > A[i][k] + A[k][j]:
                        newA[i][j] = A[i][k] + A[k][j]
                        newP[i][j] = P[k][j]
        A = newA
        P = newP
        display_matrix(A, P, n, k + 1)
    print("\nFinal Shortest Paths")
    print("src  dest  len  path")
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if A[i][j] == INF:
                print(f"{i + 1:<5}{j + 1:<6}{'inf':<5}No path")
            else:
                path = get_path(P, i, j)
                path_string = " -> ".join(str(x + 1) for x in path)

                print(f"{i + 1:<5}{j + 1:<6}{A[i][j]:<5g}{path_string}")
    return A, P
n = int(input("Enter number of vertices: "))
cost = []
print("Enter cost adjacency matrix (use inf for no edge):")
for i in range(n):
    row = input().split()
    row = [
        INF if x.lower() == "inf" else float(x)
        for x in row
    ]
    cost.append(row)
A = [[0] * n for _ in range(n)]
A, P = AllPairsSP(cost, A, n)