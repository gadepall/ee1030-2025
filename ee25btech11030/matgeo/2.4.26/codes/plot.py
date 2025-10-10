import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
triangle_lib = ctypes.CDLL("./triangle.so")

# Define function return type
triangle_lib.isosceles_triangle.argtypes = [np.ctypeslib.ndpointer(dtype=np.double,ndim=1,flags="C"),np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C")]

# Create numpy array to hold 6 values (x,y for 3 points)
points = np.zeros(6, dtype=np.double)
M = np.zeros(2, dtype=np.double)

# Call C function to fill points
triangle_lib.isosceles_triangle(points,M)

# Reshape into (3,2)
points = points.reshape((3,2))

# Close the triangle (repeat first point)
points = np.vstack([points, points[0]])

#text
plt.text(points[0,0]+0.2, points[0,1]+0.2, "A(5,-2)", fontsize=12, ha='right')
plt.text(points[1,0], points[1,1], "B(6,4)", fontsize=12, ha='right')
plt.text(points[2,0]+0.2, points[2,1]+0.2, "C(7,-2)", fontsize=12, ha='left')
plt.text(M[0]+0.2, M[1]+0.2, "M(6,-2)", fontsize=12, ha='center')

# Plot isosceles triangle
plt.plot(points[:,0], points[:,1], "bo-")
plt.plot([M[0],points[1,0]],[M[1],points[1,1]],"go-")
plt.xlim([2,9])
plt.ylim([-4,6])
plt.title("isosceles triangle from C library")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.savefig('figs/triangle.png')
plt.show()
