import numpy as np
import matplotlib.pyplot as plt

# Given points
A = np.array([3, 4, -5])
B = np.array([-2, 1, 4])

# Step 1: Compute B - A
BA = B - A

# Step 2: Left-hand row vector = 2(B - A)^T
coeff = 2 * BA

# Step 3: RHS = B^T B - A^T A
rhs = np.dot(B, B) - np.dot(A, A)

print("Equation of plane from matrix theory:")
print(f"{coeff[0]}x + {coeff[1]}y + {coeff[2]}z = {rhs}")

# Midpoint of AB
M = (A + B) / 2

# --- Plotting the plane ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Define grid for plane
x_vals = np.linspace(-6, 6, 20)
y_vals = np.linspace(-6, 6, 20)
X, Y = np.meshgrid(x_vals, y_vals)
Z = (rhs - coeff[0]*X - coeff[1]*Y) / coeff[2]

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5, color="cyan")

# Plot points A, B, and midpoint M
ax.scatter(*A, color="red", s=50, label="A(3,4,-5)")
ax.scatter(*B, color="blue", s=50, label="B(-2,1,4)")
ax.scatter(*M, color="black", s=50, label="Midpoint M")

# Plot AB line
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], "k--", label="AB")

# Labels
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.legend()

plt.title("Perpendicular Bisector Plane of A and B (Matrix Theory)")
plt.savefig("fig2.png", dpi=300, bbox_inches="tight")  # Save the figure
plt.show()
