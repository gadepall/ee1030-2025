import numpy as np
import matplotlib.pyplot as plt

# Vertices
A = np.array([2, 9])
B = np.array([2, 5])
C = np.array([5, 5])

# Check right angle at B using dot product
AB = A - B
BC = C - B
print("Dot product AB·BC =", np.dot(AB, BC))

if np.dot(AB, BC) == 0:
    print("Right angle at B ✅")

# Area using determinant formula
area = abs(np.linalg.det(np.array([
    [A[0], A[1], 1],
    [B[0], B[1], 1],
    [C[0], C[1], 1]
]))) / 2
print("Area of triangle ABC (Python):", area)

# Plot
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]

plt.plot(x, y, 'ro-')
plt.text(A[0], A[1], "A(2,9)", fontsize=10, ha="right")
plt.text(B[0], B[1], "B(2,5)", fontsize=10, ha="right")
plt.text(C[0], C[1], "C(5,5)", fontsize=10, ha="right")
plt.title("Right Triangle ABC (Pure Python)")
plt.grid(True)
plt.axis("equal")
plt.show()

