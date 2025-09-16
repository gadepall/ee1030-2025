import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Use LaTeX-compatible font settings
matplotlib.use('pgf')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "lmodern",
    "font.size": 11,
})

# Define points A and B
h, k = 5, 7
A = np.array([h, 0, 0])
B = np.array([0, k, 0])

# Compute a third point C that lies on the line AB using parameter t
t = 2  # You can change this to move along the line
C = (1 - t) * A + t * B

# Stack points for plotting
points = np.vstack([A, B, C])

# 3D Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(points[:,0], points[:,1], points[:,2], color=['red', 'green', 'blue'], s=100)
ax.plot(points[:,0], points[:,1], points[:,2], color='purple', label='Line through A, B, C')

# Annotate the points
ax.text(*A, ' A', color='red')
ax.text(*B, ' B', color='green')
ax.text(*C, ' C', color='blue')

# Axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(r'Collinear Points $(h,0,0)$, $(0,k,0)$, and $(a,b,c)$')
ax.legend()
ax.grid(True)

# Save the figure
fig.savefig("collinear_3d_plot.png")