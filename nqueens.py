x = []
count = 0
first_solution = None
def Place(k, i):
    for j in range(1, k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False
    return True
def NQueens(k, n):
    global count, first_solution
    for i in range(1, n + 1):
        if Place(k, i):
            x[k] = i
            if k == n:
                count += 1
                if first_solution is None:
                    first_solution = x[1:n + 1].copy()
            else:
                NQueens(k + 1, n)
def display_board(solution, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if solution[i - 1] == j:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()
for n in range(2, 13):
    x = [0] * (n + 1)
    count = 0
    first_solution = None
    NQueens(1, n)
    print("\nNo of queens =", n)
    if first_solution is not None:
        print("Solution 1 =", end=" ")
        for i in range(1, n + 1):
            print("x" + str(i) + "=" + str(first_solution[i - 1]), end=" ")
        print()
        print("Matrix of solution 1:")
        display_board(first_solution, n)
    else:
        print("No solution exists")
    print("No of solutions =", count)