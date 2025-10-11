import numpy as np
import matplotlib.pyplot as plt

# Points
A = np.array([3, -1, 2])
B = np.array([5,  2, 4])
C = np.array([-1, -1, 6])
O = np.array([0, 0, 0])

# Step 1: Vectors AB, AC
AB = B - A
AC = C - A

# Step 2: Normal via cross product
N = np.cross(AB, AC)
print("Normal vector N:", N)

# Step 3: Plane equation N^T x = d
d = np.dot(N, A)
print(f"Plane equation: {N}^T x = {d}")

# Step 4: Distance from origin
distance = abs(d) / np.linalg.norm(N)
print(f"Distance from origin = {distance:.4f}")

# Step 5: Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color='red', s=50, label='A(3,-1,2)')
ax.scatter(*B, color='blue', s=50, label='B(5,2,4)')
ax.scatter(*C, color='green', s=50, label='C(-1,-1,6)')
ax.scatter(*O, color='black', s=50, label='Origin')

# Plot plane
xx, yy = np.meshgrid(range(-2, 6), range(-3, 5))
zz = (d - N[0]*xx - N[1]*yy) / N[2]

ax.plot_surface(xx, yy, zz, alpha=0.4, color='cyan')

# Aesthetics
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
ax.set_title("Plane through A, B, C and its distance from origin")

plt.savefig("../figs/fig.png")
