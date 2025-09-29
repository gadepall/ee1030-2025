import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter range
t = np.linspace(-10, 10, 200)

# First line: (x, y, z) = (1+2λ, -1+3λ, 1+4λ)
x1 = 1 + 2*t
y1 = -1 + 3*t
z1 = 1 + 4*t

# Second line: (x, y, z) = (3+μ, k+2μ, μ)
# Example: set k = 2 (you can change it to the value you solve for)
k = 2
x2 = 3 + t
y2 = k + 2*t
z2 = t

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot lines
ax.plot(x1, y1, z1, label="Line 1", color="blue")
ax.plot(x2, y2, z2, label=f"Line 2 (k={k})", color="orange")

# Mark reference points
ax.scatter(1, -1, 1, color='red', s=50, label="Point on Line 1")
ax.scatter(3, k, 0, color='green', s=50, label="Point on Line 2")

# Labels & title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Plot of Two Lines")
ax.legend()
plt.show()
