import numpy as np
import matplotlib.pyplot as plt


center = (0, 0)
r_inner = 3.0
r_outer = 5.0


point_A = np.array([5.0, 0.0])


tangent_point_1 = np.array([9/5, 12/5])  # (1.8, 2.4)
tangent_point_2 = np.array([9/5, -12/5]) # (1.8, -2.4)

theta = np.linspace(0, 2 * np.pi, 200)


x_inner = center[0] + r_inner * np.cos(theta)
y_inner = center[1] + r_inner * np.sin(theta)


x_outer = center[0] + r_outer * np.cos(theta)
y_outer = center[1] + r_outer * np.sin(theta)


plt.figure(figsize=(8, 8))
ax = plt.gca()


ax.plot(x_inner, y_inner, label=f'Inner Circle (r={r_inner})', color='blue')
ax.plot(x_outer, y_outer, label=f'Outer Circle (r={r_outer})', color='orange')


ax.plot([point_A[0], tangent_point_1[0]], [point_A[1], tangent_point_1[1]], 'g-', label='Tangent 1')
ax.plot([point_A[0], tangent_point_2[0]], [point_A[1], tangent_point_2[1]], 'g-', label='Tangent 2')

ax.plot([center[0], tangent_point_1[0]], [center[1], tangent_point_1[1]], 'r--', label='Radius to Tangent Point')
ax.plot([center[0], tangent_point_2[0]], [center[1], tangent_point_2[1]], 'r--')


ax.plot(center[0], center[1], 'ko', label='Center (0,0)')
ax.plot(point_A[0], point_A[1], 'go', markersize=8, label=f'Point A {tuple(point_A)}')
ax.plot(tangent_point_1[0], tangent_point_1[1], 'ro', label='Tangent Points')
ax.plot(tangent_point_2[0], tangent_point_2[1], 'ro')

# --- 5. Final Plot Adjustments ---
# Ensure the plot has an equal aspect ratio to make circles look circular
ax.set_aspect('equal', adjustable='box')

# Add titles and labels for clarity
plt.title('Construction of Tangents to Concentric Circles')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

# Set axis limits for a nice view
plt.xlim(-6, 6)
plt.ylim(-6, 6)

plt.savefig("figure.png", dpi=300)
# Show the plot
plt.show()
