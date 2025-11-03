import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the compiled C library
lib = ctypes.CDLL('./4.11.27.so')  # or './intersection.dll' on Windows

# Prepare result array
result = (ctypes.c_double * 3)()
lib.find_intersection(result)

intersection = np.array([result[0], result[1], result[2]])
print("Intersection point:", intersection)

# Define line points
P = np.array([4, -3, -4])
Q = np.array([3, -2, 2])
line_points = np.array([P, Q])

# Plane setup
xx, yy = np.meshgrid(np.linspace(0, 5, 10), np.linspace(-5, 5, 10))
zz = 6 - 2*xx - yy  # from plane equation 2x + y + z = 6

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')
ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], color='red', label='Line PQ')
ax.scatter(intersection[0], intersection[1], intersection[2], color='blue', s=50, label='Intersection')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plot of the Intersection point ')
ax.legend()
plt.show()

