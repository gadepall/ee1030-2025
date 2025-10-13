import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library (adjust path if needed)
lib = ctypes.CDLL('./4.7.47.so')

# declare argtypes: 6 doubles for matrix and RHS, and two double* for outputs
lib.solve_system.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

# Problem data
P = np.array([2.0, 3.0])         # given point P
# Line: y = 3x + 4
# We form the 2x2 linear system derived in the method:
# [1  3] Q = [m^T P]  where m = (1,3)
# [3 -1]     [   c  ]  where c = -4 (because n = (3,-1), n^T x = c -> 3x - y = -4)
A = np.array([[1.0, 3.0],
              [3.0, -1.0]])
b = np.array([ (1.0*P[0] + 3.0*P[1]),  # m^T P = [1 3] dot P
               -4.0 ])                 # c = -4

# Prepare output doubles
rx = ctypes.c_double()
ry = ctypes.c_double()

# Call C function
lib.solve_system(A[0,0], A[0,1],
                 A[1,0], A[1,1],
                 b[0],    b[1],
                 ctypes.byref(rx), ctypes.byref(ry))

Q = np.array([rx.value, ry.value])

print("Foot of perpendicular Q =", Q)

# Plotting
x = np.linspace(-3, 4, 400)
y_line = 3*x + 4          # the line y = 3x + 4

plt.figure(figsize=(7,6))
plt.plot(x, y_line, label='Line: y = 3x + 4', linewidth=2)

# Plot the given point P and foot Q
plt.scatter([P[0]], [P[1]], marker='o', s=80, label='P (2,3)')
plt.scatter([Q[0]], [Q[1]], marker='o', s=80, label=f'Q ({Q[0]:.3f}, {Q[1]:.3f})', color='red')

# Draw the perpendicular segment PQ
plt.plot([P[0], Q[0]], [P[1], Q[1]], '--', linewidth=1.8, label='Perpendicular PQ')

# For visual reference, draw direction vector of the line at Q (scaled)
dir_vec = np.array([1.0, 3.0])
plt.arrow(Q[0], Q[1], 0.6*dir_vec[0], 0.6*dir_vec[1], head_width=0.12, head_length=0.18, length_includes_head=True)

plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(min(-3, P[0]-2), max(4, P[0]+2))
plt.ylim(min(-1, P[1]-2), max(6, P[1]+3))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Foot of Perpendicular from P')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

