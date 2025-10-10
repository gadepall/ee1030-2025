import numpy as np
import matplotlib.pyplot as plt

# angles in radians
B = np.deg2rad(60)
C = np.deg2rad(45)

# Coefficient matrix and RHS vector
A = np.array([
    [1, 1, 1],
    [-1, np.cos(C), np.cos(B)],
    [0, np.sin(C), -np.sin(B)]
], dtype=float)

rhs = np.array([12, 0, 0], dtype=float)

# Solve the linear system
a, b, c = np.linalg.solve(A, rhs)
print(f"a = {a:.3f}, b = {b:.3f}, c = {c:.3f}")

# Coordinates of vertices
B_pt = np.array([0, 0])
C_pt = np.array([a, 0])
A_pt = np.array([c*np.cos(B), c*np.sin(B)])

# Plot the triangle
x = [A_pt[0], B_pt[0], C_pt[0], A_pt[0]]
y = [A_pt[1], B_pt[1], C_pt[1], A_pt[1]]

plt.plot(x, y)
plt.scatter(x, y)

plt.text(A_pt[0], A_pt[1], "A")
plt.text(B_pt[0], B_pt[1], "B")
plt.text(C_pt[0], C_pt[1], "C")


plt.axhline(0, color='black')   # x-axis
plt.axvline(0, color='black')   # y-axis
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")

plt.savefig("../figs/fig.png", dpi=300)
