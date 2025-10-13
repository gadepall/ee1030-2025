import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of a and b values
a = np.linspace(-10, 10, 20)
b = np.linspace(-10, 10, 20)
A, B = np.meshgrid(a, b)

# Define the planes
Z1 = -7 - 1*A - 4*B   # a + 4b + z = -7 => z = -7 - a - 4b
Z2 = -8 - 2*A - 5*B   # 2a + 5b + z = -8 => z = -8 - 2a - 5b
Z3 = -9 - 3*A - 6*B   # 3a + 6b + z = -9 => z = -9 - 3a - 6b

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, B, Z1, alpha=0.5, color='red', label='Plane 1')
ax.plot_surface(A, B, Z2, alpha=0.5, color='green', label='Plane 2')
ax.plot_surface(A, B, Z3, alpha=0.5, color='blue', label='Plane 3')

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')
ax.set_title('Graph of 3 Planes')

plt.show()
