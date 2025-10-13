import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, c_double, POINTER

# Load the shared library
lib = CDLL('./4.3.40.so')

# Define function signature for line_point
lib.line_point.argtypes = [c_double, POINTER(c_double)]
lib.line_point.restype = None

def get_point(lambda_val):
    # Prepare array for results
    result = (c_double * 3)()
    lib.line_point(lambda_val, result)
    return np.array([result[0], result[1], result[2]])

# Generate points on the line for lambda in [-10, 10]
lambdas = np.linspace(-10, 10, 400)
points = np.array([get_point(l) for l in lambdas])

# Plotting the line in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(points[:,0], points[:,1], points[:,2], label='Line: r = a + λd', color='blue')

# Plot the point a
ax.scatter(2, -1, 4, color='red', label='Point a (2, -1, 4)')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('3D Line plot')
plt.show()

