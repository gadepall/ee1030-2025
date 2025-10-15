import numpy as np
import matplotlib.pyplot as plt

# Fixed Vertices
B = np.array([2, 0])
C = np.array([0, -2])

# Vertices for the two possible values of k
A1 = np.array([0, 0])  # k = 0
A2 = np.array([4, 0])  # k = 4

# --- Calculate and verify areas ---
# Area for k=0
area1 = abs(np.linalg.det(np.array([
    [A1[0], A1[1], 1],
    [B[0], B[1], 1],
    [C[0], C[1], 1]
]))) / 2
print(f"Area of triangle for k=0: {area1}")

# Area for k=4
area2 = abs(np.linalg.det(np.array([
    [A2[0], A2[1], 1],
    [B[0], B[1], 1],
    [C[0], C[1], 1]
]))) / 2
print(f"Area of triangle for k=4: {area2}")


# --- Plotting ---
# Coordinates for triangle 1 (k=0)
x1 = [A1[0], B[0], C[0], A1[0]]
y1 = [A1[1], B[1], C[1], A1[1]]

# Coordinates for triangle 2 (k=4)
x2 = [A2[0], B[0], C[0], A2[0]]
y2 = [A2[1], B[1], C[1], A2[1]]

plt.plot(x1, y1, 'ro-', label='Triangle (k=0)')
plt.plot(x2, y2, 'go-', label='Triangle (k=4)')

# Labeling points
plt.text(A1[0], A1[1] + 0.2, "A(0,0)", fontsize=10, ha="center")
plt.text(A2[0], A2[1] + 0.2, "A(4,0)", fontsize=10, ha="center")
plt.text(B[0], B[1] - 0.4, "B(2,0)", fontsize=10, ha="center")
plt.text(C[0], C[1] - 0.4, "C(0,-2)", fontsize=10, ha="center")

plt.title("Triangles with Area = 2 sq. units")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
