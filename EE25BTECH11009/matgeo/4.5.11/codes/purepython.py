import numpy as np
import matplotlib.pyplot as plt

# --- Line information ---
# Required line: passes through A(-2,4,-5)
point_A = np.array([-2, 4, -5])

# Given line: passes through P(-3,4,-8)
point_P = np.array([-3, 4, -8])

# Direction vector (same for both lines)
direction_vector = np.array([3, 5, 6])

print(f"Point A (Required Line): {point_A}")
print(f"Point P (Given Line): {point_P}")
print(f"Direction Vector (m): {direction_vector}")

# --- Parametric equations ---
lam = np.linspace(-5, 5, 100)

# Required line through A
x_A = point_A[0] + lam * direction_vector[0]
y_A = point_A[1] + lam * direction_vector[1]
z_A = point_A[2] + lam * direction_vector[2]

# Given line through P
x_P = point_P[0] + lam * direction_vector[0]
y_P = point_P[1] + lam * direction_vector[1]
z_P = point_P[2] + lam * direction_vector[2]

# --- Plotting ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the required line (Blue)
ax.plot(x_A, y_A, z_A, label='Required Line (through A)', color='blue')
ax.scatter(point_A[0], point_A[1], point_A[2],
           color='purple', s=50, label='Point A (-2,4,-5)')
ax.quiver(point_A[0], point_A[1], point_A[2],
          direction_vector[0], direction_vector[1], direction_vector[2],
          color='green', arrow_length_ratio=0.1, label='Direction Vector at A')

# Plot the given line (Red dashed)
ax.plot(x_P, y_P, z_P, '--', label='Given Line (through P)', color='red')
ax.scatter(point_P[0], point_P[1], point_P[2],
           color='orange', s=50, label='Point P (-3,4,-8)')
ax.quiver(point_P[0], point_P[1], point_P[2],
          direction_vector[0], direction_vector[1], direction_vector[2],
          color='black', arrow_length_ratio=0.1, label='Direction Vector at P')

# Labels and title
ax.set_title('Required Line and Given Line (Parallel)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

# Equal aspect ratio for better geometry
ax.set_box_aspect([1,1,1])
plt.savefig("../figs/Figure_2.png")
plt.show()
