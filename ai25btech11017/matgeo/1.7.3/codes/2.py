import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Points
A = np.array([-2, 3, 5])
B = np.array([1, 2, 3])
C = np.array([7, 0, -1])

# Direction vector AB
AB = B - A

# Generate line through A in direction AB
t = np.linspace(-1, 3, 100)  # parameter
line = A[:, None] + AB[:, None] * t

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color='red', label='A(-2,3,5)', s=50)
ax.scatter(*B, color='blue', label='B(1,2,3)', s=50)
ax.scatter(*C, color='green', label='C(7,0,-1)', s=50)

# Plot line through A, B, C
ax.plot(line[0], line[1], line[2], color='black', linestyle='--', label='Line through A, B, C')

# Labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()

# Save figure
plt.savefig("/home/balu/matgeo/figs/fig.png", dpi=300)
plt.show()

