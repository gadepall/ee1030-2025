import ctypes
import matplotlib.pyplot as plt

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float), ("y", ctypes.c_float)]

# Load the shared library
lib = ctypes.CDLL('./libgeometry.so')

lib.midpoint.argtypes = [Point, Point]
lib.midpoint.restype = Point

# Define wrapper
def midpoint(a, b):
    return lib.midpoint(a, b)

# Define rectangle points
A = Point(-1, -1)
B = Point(-1, 6)
C = Point(3, 6)
D = Point(3, -1)

# Midpoints
P = lib.midpoint(A, B)
Q = lib.midpoint(B, C)
R = lib.midpoint(C, D)
S = lib.midpoint(D, A)

# Plotting
points = [P, Q, R, S, P]  # Loop back to P
x_vals = [p.x for p in points]
y_vals = [p.y for p in points]
plt.plot(x_vals, y_vals, marker='o', label='PQRS')

# Diagonal from P to R
plt.plot([P.x, R.x], [P.y, R.y], 'r--', label='Diagonal PR')

# Diagonal from Q to S
plt.plot([Q.x, S.x], [Q.y, S.y], 'g--', label='Diagonal QS')

plt.title("Quadrilateral PQRS")
plt.grid(True)
plt.axis('equal')
plt.show()

