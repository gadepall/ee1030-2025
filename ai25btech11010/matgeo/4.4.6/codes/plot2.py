import os
import numpy as np
import matplotlib.pyplot as plt

# Ensure 'figs' folder exists
os.makedirs("figs", exist_ok=True)

# Run the C program
stream = os.popen('./plane')   # Execute the C program
output = stream.read()
stream.close()

# Read normal vector and d from C output
n1, n2, n3, d = map(float, output.split())
print("Normal vector:", n1, n2, n3)
print("Plane equation: {:.2f}x + {:.2f}y + {:.2f}z = {:.2f}".format(n1, n2, n3, d))

# Load points from .dat file
points = np.loadtxt('plane_points.dat', comments="#")

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points and annotate coordinates
for x, y, z in points:
    ax.scatter(x, y, z, color='red', s=50)
    ax.text(x, y, z, f'({x},{y},{z})', color='black')

# Plot plane
x = np.linspace(min(points[:,0])-1, max(points[:,0])+1, 10)
y = np.linspace(min(points[:,1])-1, max(points[:,1])+1, 10)
X, Y = np.meshgrid(x, y)
Z = (d - n1*X - n2*Y)/n3

ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Plane through points A, B, C with coordinates')

# Save plot as PNG in 'figs' folder
plt.savefig("../figs/plane_plot2.png", dpi=300)
print("Plot saved as figs/plane_plot.png")

plt.show()
