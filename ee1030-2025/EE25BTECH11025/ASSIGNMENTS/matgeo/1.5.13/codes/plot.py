import sys
import numpy as np
import matplotlib.pyplot as plt

# Add your workspace path (adjust if needed)
sys.path.insert(0, '/home/ganachari-vishwmabhar/Downloads/codes/CoordGeo')

# Local imports
from line.funcs import line_gen

# Read intersection point from values.dat (skip first two rows if it has header)
data = np.loadtxt("values.dat", skiprows=2)
xc, yc = data[0], data[1]
C = np.array([xc, yc]).reshape(-1, 1)

# Given points
A = np.array([-1, -4]).reshape(-1, 1)
B = np.array([5, -6]).reshape(-1, 1)

# Generate line AB using helper function
x_AB = line_gen(A, B)

# ---- Plotting ----
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')

# Collect points
tri_coords = np.block([A, B, C])
plt.scatter(tri_coords[0, :], tri_coords[1, :])

# Labels
vert_labels = ['A(-1,-4)', 'B(5,-6)', f'C({xc:.2f},{yc:.2f})']

for i, txt in enumerate(vert_labels):
    x, y = tri_coords[:, i]
    plt.annotate(txt, (x, y),
                 textcoords="offset points",
                 xytext=(10, -10),
                 ha='center')

# Axes styling
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Intersection of line AB with Y-axis")

# Save & Show
plt.savefig('../figs/fig1.png')
plt.show()

