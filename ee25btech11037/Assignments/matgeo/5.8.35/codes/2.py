import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Define planes ---
# Plane 1: 4x + 3y + 2z = 60
# Plane 2: 2x + 4y + 6z = 90
# Plane 3: 6x + 2y + 3z = 70

A = np.array([
    [4.0, 3.0, 2.0],
    [2.0, 4.0, 6.0],
    [6.0, 2.0, 3.0]
], dtype=float)

b = np.array([60.0, 90.0, 70.0], dtype=float)

# Solve for intersection point
sol = np.linalg.solve(A, b)  # [x, y, z]
print(f"Intersection point: ({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})")

# --- Plot planes ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Axes range
x_vals = np.linspace(0, 15, 20)
y_vals = np.linspace(0, 15, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# Plane equations
Z1 = (60 - 4*X - 3*Y) / 2
Z2 = (90 - 2*X - 4*Y) / 6
Z3 = (70 - 6*X - 2*Y) / 3

# Plot planes
ax.plot_surface(X, Y, Z1, alpha=0.2, color='red')
ax.plot_surface(X, Y, Z2, alpha=0.2, color='green')
ax.plot_surface(X, Y, Z3, alpha=0.2, color='blue')

# Plot intersection point
ax.scatter(sol[0], sol[1], sol[2], color='black', s=100, label=f"Intersection ({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})")

# Label planes
ax.text(10, 0, (60 - 4*10 - 3*0)/2 + 1, "4x + 3y + 2z = 60", color="red", fontsize=10)
ax.text(0, 10, (90 - 2*0 - 4*10)/6 + 1, "2x + 4y + 6z = 90", color="green", fontsize=10)
ax.text(10, 10, (70 - 6*10 - 2*10)/3 + 1, "6x + 2y + 3z = 70", color="blue", fontsize=10)

# Annotate intersection point in white
ax.text(sol[0], sol[1], sol[2]+0.5,
        f"({sol[0]:.2f}, {sol[1]:.2f}, {sol[2]:.2f})",
        color="white", fontsize=10)

# Axes labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Planes and Intersection Point")


ax.legend()
plt.savefig('2.png')
plt.show()

