import numpy as np
import matplotlib.pyplot as plt
import ctypes

# ------------------------
# Load C library to get normal vector
# ------------------------
lib = ctypes.CDLL("./points.so")
n1 = ctypes.c_double()
n2 = ctypes.c_double()
lib.get_normal_vector(ctypes.byref(n1), ctypes.byref(n2))
print("Normal vector from C:", n1.value, n2.value)

# ------------------------
# Points A and B
# ------------------------
A = np.array([3, 1])
B = np.array([9, 3])

# Direction vector along line
D = B - A

# Parameter t for plotting line
t = np.linspace(-1, 2, 100)
line_points = A[:, None] + D[:, None]*t

# ------------------------
# Plot line and points in 2D
# ------------------------
plt.figure(figsize=(6,6))
plt.plot(line_points[0], line_points[1], color='r', label='Line through A and B')
plt.scatter([A[0], B[0]], [A[1], B[1]], color='b', s=50, label='Points A and B')

# Optional: plot normal vector from origin
origin = np.array([0,0])
plt.quiver(*origin, n1.value, n2.value, angles='xy', scale_units='xy', scale=1,
           color='g', label='Normal vector')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line and Normal Vector for Points (3,1) & (9,3)')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.savefig("line_normal_2d.png")
plt.show()

