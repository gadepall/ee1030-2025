import numpy as np
import matplotlib.pyplot as plt

# Parameter range
t = np.linspace(-5, 5, 100)

# Line L1: (x,y,z) = (1,1,-1) + λ(3,-1,0)
x1 = 1 + 3*t
y1 = 1 - t
z1 = -1 * np.ones_like(t)

# Line L2: (x,y,z) = (-4,0,-1) + μ(2,0,3)
x2 = -4 + 2*t
y2 = np.zeros_like(t)
z2 = -1 + 3*t

# Create 3D plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plot the two lines
ax.plot(x1, y1, z1, label="Line L1: (1,1,-1)+λ(3,-1,0)", color='blue')
ax.plot(x2, y2, z2, label="Line L2: (-4,0,-1)+μ(2,0,3)", color='red')

# Mark given points
ax.scatter(1, 1, -1, color='blue', s=50, marker='o')
ax.text(1, 1, -1, "(1,1,-1)", color='blue')

ax.scatter(-4, 0, -1, color='red', s=50, marker='o')
ax.text(-4, 0, -1, "(-4,0,-1)", color='red')

# Labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Skew Lines in 3D")
ax.legend()

plt.show()
