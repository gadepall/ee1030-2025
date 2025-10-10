import numpy as np
import matplotlib.pyplot as plt

# Vertices
A = np.array([4, 6])
B = np.array([1, 5])
C = np.array([7, 2])

# Points D and E using section formula (1:2)
D = (2*A + B)/3
E = (2*A + C)/3

# Function to calculate area of triangle given 3 points
def area(P, Q, R):
    return 0.5 * np.linalg.norm(np.linalg.det(np.array([
        [Q[0] - P[0], R[0] - P[0]],
        [Q[1] - P[1], R[1] - P[1]]
    ])))

# Areas
area_ABC = area(A, B, C)
area_ADE = area(A, D, E)

# Ratio
ratio = area_ADE / area_ABC

# Print solution
print("Area of ΔABC =", area_ABC)
print("Area of ΔADE =", area_ADE)
print("Ratio ΔADE/ΔABC =", ratio)

# Plotting
plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'k-', label='Triangle ABC')
plt.plot([A[0], D[0]], [A[1], D[1]], 'r--')
plt.plot([A[0], E[0]], [A[1], E[1]], 'r--')
plt.plot([D[0], E[0]], [D[1], E[1]], 'r--', label='Triangle ADE')

points = np.vstack([A, B, C, D, E])
labels = ['A(4,6)', 'B(1,5)', 'C(7,2)', 'D(3,17/3)', 'E(5,14/3)']

plt.scatter(points[:, 0], points[:, 1], color='black')
for i, txt in enumerate(labels):
    plt.annotate(txt, (points[i, 0], points[i, 1]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.gca().set_aspect('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid(True)

plt.savefig('fig4.png')
plt.show()