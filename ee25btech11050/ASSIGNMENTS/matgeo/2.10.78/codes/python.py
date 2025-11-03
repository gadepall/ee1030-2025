import numpy as np
import matplotlib.pyplot as plt

# Step 0: Initial point
P = np.array([4.0, 1.0])
points = [P]
labels = ["Original (4,1)"]

# Step 1: Reflection about the line y = x
# Matrix: [[0, 1], [1, 0]]
reflect_matrix = np.array([[0, 1],
                           [1, 0]])
P1 = reflect_matrix @ P
points.append(P1)
labels.append("After Reflection")

# Step 2: Translation by 2 units along +x-axis
# Use homogeneous coordinates: convert P1 to 3D vector
P1_h = np.array([P1[0], P1[1], 1.0])
translate_matrix = np.array([[1, 0, 2],
                             [0, 1, 0],
                             [0, 0, 1]])
P2_h = translate_matrix @ P1_h
P2 = P2_h[:2]
points.append(P2)
labels.append("After Translation")

# Step 3: Rotation by π/4 counter-clockwise
theta = np.pi / 4
cos_t = np.cos(theta)
sin_t = np.sin(theta)
rotate_matrix = np.array([[cos_t, -sin_t],
                          [sin_t, cos_t]])
P3 = rotate_matrix @ P2
points.append(P3)
labels.append("After Rotation ")

# Convert all points to a NumPy array
points = np.array(points)

# Plotting
colors = ['blue', 'orange', 'green', 'red']
plt.figure(figsize=(8, 8))
for i, point in enumerate(points):
    plt.plot(point[0], point[1], 'o', color=colors[i], label=labels[i])
    plt.text(point[0] + 0.2, point[1] + 0.2, f"{labels[i]}\n({point[0]:.2f}, {point[1]:.2f})")

# Draw arrows between steps
for i in range(len(points) - 1):
    plt.arrow(points[i][0], points[i][1],
              points[i+1][0] - points[i][0],
              points[i+1][1] - points[i][1],
              head_width=0.2, length_includes_head=True,
              fc='gray', ec='gray', linestyle='dashed')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.title("Transformations of Point (4, 1)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Final output
print(f"Final coordinates: ({P3[0]:.4f}, {P3[1]:.4f})")

