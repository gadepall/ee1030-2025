import numpy as np
import matplotlib.pyplot as plt

# Points
A = np.array([2, 5])
B = np.array([4, 7])
C = np.array([6, 2])

# Area using determinant method
matrix = np.array([
    [A[0], A[1], 1],
    [B[0], B[1], 1],
    [C[0], C[1], 1]
])
area = 0.5 * abs(np.linalg.det(matrix))
print(f"Area of triangle ABC = {area:.2f}")

# Plot triangle
x_coords = [A[0], B[0], C[0], A[0]]
y_coords = [A[1], B[1], C[1], A[1]]

plt.plot(x_coords, y_coords, 'b-', label='Triangle ABC')
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')

# Annotate points
labels = ['A(2,5)', 'B(4,7)', 'C(6,2)']
for (x, y), label in zip([A, B, C], labels):
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(5,5), ha='center')

plt.title("Triangle ABC")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.savefig("triangle.png")
plt.show()
