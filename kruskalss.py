def adjust(A, i, n):
    j = 2 * i
    item = A[i]

    while j <= n:
        if j < n and A[j][0] > A[j + 1][0]:
            j = j + 1

        if item[0] <= A[j][0]:
            break

        A[j // 2] = A[j]
        j = 2 * j

    A[j // 2] = item


def heapify(A, n):
    for i in range(n // 2, 0, -1):
        adjust(A, i, n)


def del_min(A, n):
    if n == 0:
        return None

    x = A[1]
    A[1] = A[n]
    A.pop()

    if n > 1:
        adjust(A, 1, n - 1)

    return x


def kruskal(E, cost, n, t):

    parent = [-1] * n

    def find(i):
        while parent[i] >= 0:
            i = parent[i]
        return i

    def union(i, j):
        parent[i] = j

    # Construct heap
    heap = [None]

    for i in range(len(E)):
        u, v = E[i]
        heap.append((cost[i], u, v))

    heapify(heap, len(E))

    i = 0
    mincost = 0
    heap_size = len(E)

    while i < n - 1 and heap_size > 0:

        edge = del_min(heap, heap_size)
        heap_size -= 1

        c, u, v = edge

        j = find(u)
        k = find(v)

        if j != k:
            i += 1

            t.append((u, v))
            mincost += c

            union(j, k)

            print(f"\nStep {i}")
            print("t        t[1,2]")
            print("-------------------")

            for x in range(len(t)):
                u1, v1 = t[x]
                print(f"{x + 1:<8} ({u1 + 1},{v1 + 1})")

            print(f"Mincost = {mincost:g}")

    if i != n - 1:
        print("\nNo Spanning Tree")
    else:
        print("\nMinimum Cost:", mincost)

    return mincost


# Input

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

E = []
cost = []

print("Enter edges and cost (u v cost):")

for i in range(e):
    u, v, c = input().split()

    E.append((int(u) - 1, int(v) - 1))
    cost.append(float(c))


t = []

kruskal(E, cost, n, t)