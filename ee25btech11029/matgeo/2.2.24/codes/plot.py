import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
square_lib = ctypes.CDLL("./square.so")

# Define function return type
square_lib.get_square_points.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C")]

# Create numpy array to hold 8 values (x,y for 4 points)
points = np.zeros(8, dtype=np.double)

# Call C function to fill points
square_lib.get_square_points(points)

# Reshape into (4,2)
points = points.reshape((4,2))

# Close the square (repeat first point)
points = np.vstack([points, points[0]])

# Plot square
plt.plot(points[:,0], points[:,1], "bo-")
plt.title("Square from C library")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.savefig('figs/square.png')
plt.show()
