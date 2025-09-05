import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
import os

# -----------------------------------------------------------
# Step 0: Ensure figs/ folder exists
# -----------------------------------------------------------
os.makedirs("figs", exist_ok=True)

# -----------------------------------------------------------
# Step 1: Define points A, B, C
# -----------------------------------------------------------
A = np.array([2, -3, 4], dtype=float)
B = np.array([-1, 2, 1], dtype=float)
C = np.array([0, 1/3, 2], dtype=float)

print("A =", A)
print("B =", B)
print("C =", C)

# -----------------------------------------------------------
# Step 2: Direction vectors AB, AC
# -----------------------------------------------------------
AB = B - A
AC = C - A

print("Vector AB =", AB)
print("Vector AC =", AC)

# -----------------------------------------------------------
# Step 3: Build matrix M with columns AB and AC
# -----------------------------------------------------------
M = np.column_stack((AB, AC))
print("Matrix M =\n", M)

# -----------------------------------------------------------
# Step 4: Row Echelon Form (Gaussian elimination)
# -----------------------------------------------------------
def row_echelon(A):
    A = A.astype(float)
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        pivot = np.argmax(np.abs(A[r:, c])) + r
        if abs(A[pivot, c]) < 1e-8:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        for i in range(r+1, rows):
            factor = A[i, c] / A[r, c]
            A[i, c:] -= factor * A[r, c:]
        r += 1
    return A, r

echelon, rank = row_echelon(M.copy())
print("Row Echelon Form of M:\n", echelon)
print("Rank(M) =", rank)

# -----------------------------------------------------------
# Step 5: Visualization
# -----------------------------------------------------------
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

# Plot points
ax.scatter(*A, color='r', label='A(2,-3,4)')
ax.scatter(*B, color='g', label='B(-1,2,1)')
ax.scatter(*C, color='b', label='C(0,1/3,2)')

# Draw line through A & B
t = np.linspace(-1, 2, 10)
line_x = A[0] + t * (B[0] - A[0])
line_y = A[1] + t * (B[1] - A[1])
line_z = A[2] + t * (B[2] - A[2])
ax.plot(line_x, line_y, line_z, 'k--', label='Line through A,B')

# Labels and style
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Collinearity of A, B, C')
ax.legend()

mp.use("TkAgg")
plt.grid(True)

# Save figure inside figs/
plt.savefig("figs/image.png", dpi=300, bbox_inches='tight')
plt.show()

