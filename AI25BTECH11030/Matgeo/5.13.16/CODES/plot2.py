import numpy as np
import matplotlib.pyplot as plt
import numpy.ctypeslib as npct
from ctypes import CDLL

# Load the shared library
lib = CDLL('./libmatfun.so')

array1d = npct.ndpointer(dtype=np.float64, ndim=1, shape=(2,))

lib.foot_of_perpendicular.restype = None
lib.foot_of_perpendicular.argtypes = [array1d, array1d, array1d, array1d]
lib.orthocenter.restype = None
lib.orthocenter.argtypes = [array1d, array1d, array1d, array1d]

A = np.array([2.0, -6.0])
B = np.array([5.0, 2.0])
C = np.array([-2.0, 2.0])

def foot_of_perpendicular(P, Q, R):
    foot = np.zeros(2, dtype=np.float64)
    lib.foot_of_perpendicular(P, Q, R, foot)
    return foot

def calc_orthocenter(A, B, C):
    O = np.zeros(2, dtype=np.float64)
    lib.orthocenter(A, B, C, O)
    return O

def plot_altitude(vertex, foot, label):
    plt.plot([vertex[0], foot[0]], [vertex[1], foot[1]], linestyle='--', label=label)

footA = foot_of_perpendicular(A, B, C)
footB = foot_of_perpendicular(B, A, C)
footC = foot_of_perpendicular(C, A, B)

O = calc_orthocenter(A, B, C)

# Print orthocenter
print(f"Orthocenter: {O}")

# Plot triangle
triangle_x = [A[0], B[0], C[0], A[0]]
triangle_y = [A[1], B[1], C[1], A[1]]
plt.plot(triangle_x, triangle_y, 'bo-', label='Triangle')

# Plot the altitudes
plot_altitude(A, footA, 'Altitude from A')
plot_altitude(B, footB, 'Altitude from B')
plot_altitude(C, footC, 'Altitude from C')

# Plot orthocenter
plt.plot(O[0], O[1], 'ro', label='Orthocenter')

plt.axis('equal')
plt.title('Triangle and Orthocenter with Altitudes')
plt.legend()
plt.grid(True)
plt.show()

