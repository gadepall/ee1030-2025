
import sys
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from line.funcs import line_gen

# Points A and B
A = np.array([-2, 4, 7]).reshape(-1, 1)
B = np.array([3, -5, 8]).reshape(-1, 1)

# Compute parameter lambda (t) where line intersects x=0 plane (YZ-plane)
t = 2/5  # from solution

# Intersection point P
P = (1 - t) * A + t * B

# Ratio AP:PB = 2:3
ratio_str = "2 : 3"

# Generate line segment AB points for plotting
line_AB = line_gen(A, B)

# Plotting setup
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Plot line AB
ax.plot(line_AB[0,:], line_AB[1,:], line_AB[2,:], label='Line AB', color='blue')

# Function to annotate points
def annotate_3d_point(ax, point, label, color):
    ax.scatter(point[0], point[1], point[2], color=color, s=80, label=label)
    ax.text(point[0], point[1], point[2] + 0.3,
            f"{label}\n({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})",
            fontsize=10, color=color)

# Plot and annotate points A, B, and P
annotate_3d_point(ax, A.flatten(), 'A', 'green')
annotate_3d_point(ax, B.flatten(), 'B', 'red')
annotate_3d_point(ax, P.flatten(), 'P', 'black')

# Plot YZ-plane (x=0)
y = np.linspace(-6, 6, 20)
z = np.linspace(5, 10, 20)
Y, Z = np.meshgrid(y, z)
X = np.zeros_like(Y)
ax.plot_surface(X, Y, Z, alpha=0.3, color='cyan')

# Add text box with ratio info
ax.text2D(0.05, 0.95,
          f"Parameter λ = {t}\nRatio AP : PB = {ratio_str}\nP lies on YZ-plane (x=0)",
          transform=ax.transAxes, fontsize=12,
          bbox=dict(facecolor='white', alpha=0.7))

# Labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of line segment AB with YZ-plane')

ax.legend()
ax.grid(True)
ax.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()

