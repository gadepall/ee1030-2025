import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
matfun_lib = ctypes.CDLL("./matfun.so")

# Define argument types for the C function
# void foot_of_perpendicular_to_Y_axis(const double P[3], double Q[3])
matfun_lib.foot_of_perpendicular_to_Y_axis.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS")
]

# Input point P
P = np.array([2.0, -3.0, 4.0], dtype=np.double)
Q = np.zeros(3, dtype=np.double)  # Output array

# Call the C function to compute the foot of perpendicular
matfun_lib.foot_of_perpendicular_to_Y_axis(P, Q)

# Y-axis vector for plotting
y_axis = np.array([[0, 0], [min(P[1], Q[1]) - 1, max(P[1], Q[1]) + 1], [0, 0]])

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(P[0], P[1], P[2], color='r', s=100, label='Point P (2, -3, 4)')
ax.scatter(Q[0], Q[1], Q[2], color='g', s=100, label='Foot of perpendicular Q')
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], color='b', label='Perpendicular')
ax.plot(y_axis[0], y_axis[1], y_axis[2], color='k', linestyle='--', label='Y axis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Foot of Perpendicular from P to Y axis')
ax.legend()
ax.view_init(elev=20, azim=45)

plt.savefig('foot_of_perpendicular_from_c.png')
plt.show()
