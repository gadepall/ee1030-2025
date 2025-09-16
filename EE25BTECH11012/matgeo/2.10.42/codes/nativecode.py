import matplotlib.pyplot as plt
import numpy as np

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# --- 1. Define three unit coplanar vectors (a, b, c) ---
# For simplicity, we'll place them on the x-y plane (z=0).
# These are just example vectors that satisfy the conditions.
a = np.array([1, 0, 0])
b = np.array([np.cos(np.pi/3), np.sin(np.pi/3), 0])  # 60 degrees from a
c = np.array([np.cos(2*np.pi/3), np.sin(2*np.pi/3), 0]) # 120 degrees from a

# --- 2. Calculate the derived vectors (v1, v2, v3) ---
v1 = 2 * a - b
v2 = 2 * b - c
v3 = 2 * c - a

# --- 3. Plot the vectors ---
# Origin point
origin = np.array([0, 0, 0])

# Plot initial vectors a, b, c
ax.quiver(*origin, *a, color='r', label='a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='g', label='b', arrow_length_ratio=0.1)
ax.quiver(*origin, *c, color='b', label='c', arrow_length_ratio=0.1)

# Plot derived vectors v1, v2, v3
ax.quiver(*origin, *v1, color='orange', label='v1 = 2a - b', arrow_length_ratio=0.1, linestyle='--')
ax.quiver(*origin, *v2, color='purple', label='v2 = 2b - c', arrow_length_ratio=0.1, linestyle='--')
ax.quiver(*origin, *v3, color='cyan', label='v3 = 2c - a', arrow_length_ratio=0.1, linestyle='--')

# --- 4. Add labels for each vector ---
ax.text(*(a*1.1), 'a', color='r', fontsize=12)
ax.text(*(b*1.1), 'b', color='g', fontsize=12)
ax.text(*(c*1.1), 'c', color='b', fontsize=12)
ax.text(*(v1*1.05), 'v1', color='orange', fontsize=12)
ax.text(*(v2*1.05), 'v2', color='purple', fontsize=12)
ax.text(*(v3*1.05), 'v3', color='cyan', fontsize=12)

# --- 5. Visualize the plane ---
# Create a grid for the plane at z=0
xx, yy = np.meshgrid(np.linspace(-3, 3, 2), np.linspace(-3, 3, 2))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.1, color='gray')


# --- 6. Set plot aesthetics ---
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Visualization of Coplanar Vectors')
ax.legend()
ax.grid(True)

# Set a viewing angle for better perspective
ax.view_init(elev=25, azim=30)

plt.show()