import numpy as np
import matplotlib.pyplot as plt

# Solve directly
p = 1
print(f"Solution from Python: p = {p}")

# Vectors
m1 = np.array([-3, p, 2])
m2 = np.array([-3*p, 1, -5])

# Dot product
dot_val = np.dot(m1, m2)
print(f"Dot product (should be 0): {dot_val}")

# Plot
fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection="3d")

origin = np.array([0, 0, 0])

ax.quiver(*origin, *m1, color="blue", linewidth=2, arrow_length_ratio=0.1, label="m1")
ax.quiver(*origin, *m2, color="red", linewidth=2, arrow_length_ratio=0.1, label="m2")

# Axes
axis_len = 6
ax.quiver(0,0,0, axis_len,0,0, color="black", arrow_length_ratio=0.05)
ax.quiver(0,0,0, 0,axis_len,0, color="black", arrow_length_ratio=0.05)
ax.quiver(0,0,0, 0,0,axis_len, color="black", arrow_length_ratio=0.05)

ax.text(axis_len, 0, 0, "X", color="black")
ax.text(0, axis_len, 0, "Y", color="black")
ax.text(0, 0, axis_len, "Z", color="black")

ax.set_xlim([-6,6])
ax.set_ylim([-6,6])
ax.set_zlim([-6,6])
ax.set_box_aspect([1,1,1])

ax.set_title("Direction Vectors (Lines Perpendicular at p=1)")
ax.legend()

plt.show()
