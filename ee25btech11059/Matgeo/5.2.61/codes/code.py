def gaussian_elimination(A):
    N = len(A)
    # Forward elimination
    for i in range(N - 1):
        for k in range(i + 1, N):
            factor = A[k][i] / A[i][i]
            for j in range(i, N + 1):
                A[k][j] -= factor * A[i][j]

    # Back substitution
    x = [0 for _ in range(N)]
    for i in range(N - 1, -1, -1):
        x[i] = A[i][N]
        for j in range(i + 1, N):
            x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x

# Augmented matrix for the system:
# x - y + 2z = 1
#    2y - 3z = 1
# 3x - 2y + 4z = 2

A = [
    [1, -1,  2, 1],
    [0,  2, -3, 1],
    [3, -2,  4, 2]
]

solution = gaussian_elimination(A)
print(f'Solution:')
print(f'x = {solution[0]}')
print(f'y = {solution[1]}')
print(f'z = {solution[2]}')

