# Code by Unnathi Garige
# Plots a 3D unit vector u = (6/7)i - (3/7)j + (2/7)k

import numpy as np
import matplotlib.pyplot as plt



data = np.loadtxt("values.dat", skiprows=1)  

xc = data[0]
yc = data[1]
zc = data[2]

# Define the unit vector
u = np.array([xc,yc,zc])

# Origin
O = np.array([0, 0, 0])

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector as an arrow
ax.quiver(O[0], O[1], O[2], u[0], u[1], u[2], 
          color='blue', linewidth=2, arrow_length_ratio=0.1, label=r'$\vec{u}$')

# Scatter points (origin and tip of vector)
ax.scatter([O[0], u[0]], [O[1], u[1]], [O[2], u[2]], color='red')

# Label tip
ax.text(u[0], u[1], u[2], r'$\vec{u}$', fontsize=12)

# Axis labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Unit vector a+b")
ax.legend()
ax.grid(True)

# Set equal aspect ratio for clarity
ax.set_box_aspect([1,1,1])

# Save and Show
plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/1.11.14/figs/fig.png')
plt.show()

