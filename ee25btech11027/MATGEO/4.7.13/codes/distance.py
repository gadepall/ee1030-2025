import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load shared C library
lib = ctypes.CDLL("./distance.so")
lib.main()

# Define points and direction vector (same as in C)
A = np.array([1,2,-4])
B = np.array([3,3,-5])
d = np.array([2,3,6])

# Generate points for both lines
t = np.linspace(-2,2,10)
line1 = A[:,None] + d[:,None]*t
line2 = B[:,None] + d[:,None]*t

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Lines
ax.plot(line1[0], line1[1], line1[2], 'b-', label='Line l1')
ax.plot(line2[0], line2[1], line2[2], 'g-', label='Line l2')

# Points
ax.scatter(*A,color='r',s=50)
ax.text(*A,"A(1,2,-4)",color='red')
ax.scatter(*B,color='orange',s=50)
ax.text(*B,"B(3,3,-5)",color='orange')

# Dotted line AB
ax.plot([A[0],B[0]], [A[1],B[1]], [A[2],B[2]], 'k--', label='Connecting AB')

ax.set_title("Figure")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/4.7.13/figs/figure1.png")
plt.show()
