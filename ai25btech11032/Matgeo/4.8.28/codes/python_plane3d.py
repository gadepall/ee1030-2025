import numpy as np
import matplotlib.pyplot as plt

# --- Input data ---
n1 = np.array([1.0, 1.0, 1.0])
n2 = np.array([2.0, 3.0, -1.0])
c1, c2 = 1.0, -4.0
ex = np.array([1.0, 0.0, 0.0])   # x-axis direction

# --- Step 1: find k ---
k = -np.dot(ex, n1) / np.dot(ex, n2)

# --- Step 2: compute plane normal and constant ---
n = n1 + k*n2
C = c1 + k*c2

# --- Step 3: distance formula ---
dist = abs(C)/np.linalg.norm(n)

# --- Step 4: foot of perpendicular from origin to plane ---
foot = (C/np.dot(n, n)) * n

print("k =", k)
print("plane normal =", n)
print("C =", C)
print("distance from x-axis =", dist)
print("foot of perpendicular =", foot)

# --- Plotting ---
fig = plt.figure(figsize=(8,7))
ax = fig.add_subplot(111, projection='3d')

# Plot the x-axis (red line)
x_line = np.linspace(-6,6,50)
ax.plot(x_line, np.zeros_like(x_line), np.zeros_like(x_line),
        color='r', lw=3, label="x-axis")

# Plot the plane (cyan surface)
xx, zz = np.meshgrid(np.linspace(-6,6,30), np.linspace(-6,6,30))
yy = (C - n[0]*xx - n[2]*zz)/n[1]
ax.plot_surface(xx, yy, zz, alpha=0.6, color='cyan')

# Plot perpendicular line (black dashed) and foot point (black dot)
ax.plot([0, foot[0]], [0, foot[1]], [0, foot[2]], 'k--', lw=2, label="perpendicular")
ax.scatter(*foot, color='k', s=50)

# Styling
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Plane (cyan) & x-axis (red)\nPerpendicular distance = {dist:.3f}")
ax.legend()
ax.view_init(elev=18, azim=60)
ax.set_box_aspect([1,1,1])  # equal aspect ratio

plt.tight_layout()
plt.savefig("new_plane.png")
plt.show()

