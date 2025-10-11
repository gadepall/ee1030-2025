import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Define a ctypes Structure that mirrors the C struct
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# --- Load the C library ---
c_lib = ctypes.CDLL('./circle.so')

# --- Define the C function's argument and return types ---
c_lib.solve_circle_tangency.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    Point, ctypes.c_double,
    ctypes.POINTER(Point), ctypes.POINTER(Point)
]
c_lib.solve_circle_tangency.restype = None

# --- Numerical Inputs are defined in Python using NumPy ---
G1, H1, K1 = -2.0, -4.0, -20.0
p_tangency_np = np.array([5.0, 5.0])
r1, r2 = 5.0, 5.0
# ---------------------------------------------------------

# --- Prepare data for C function call ---
# 1. Convert NumPy array to the ctypes Point structure
p_tangency_ctypes = Point(x=p_tangency_np[0], y=p_tangency_np[1])

# 2. Prepare empty ctypes structures to receive the output
c1_center_ctypes = Point()
c2_center_ctypes = Point()

# --- Call the C function ---
c_lib.solve_circle_tangency(
    G1, H1, K1, p_tangency_ctypes, r2, 
    ctypes.byref(c1_center_ctypes), 
    ctypes.byref(c2_center_ctypes)
)

# --- Convert results from ctypes back to NumPy arrays ---
c1 = np.array([c1_center_ctypes.x, c1_center_ctypes.y])
c2 = np.array([c2_center_ctypes.x, c2_center_ctypes.y])
p = p_tangency_np # Use the original numpy array

# --- Plotting with NumPy arrays ---
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the circles
circle1 = plt.Circle(c1, r1, fill=False, edgecolor='gray', linestyle='--')
circle2 = plt.Circle(c2, r2, fill=False, edgecolor='gray', linestyle='-')
ax.add_patch(circle1)
ax.add_patch(circle2)

# Plot the line connecting centers
ax.plot([c1[0], c2[0]], [c1[1], c2[1]], 'b-', label='Line of Centers')

# Plot the key points
ax.plot(c1[0], c1[1], 'ro', markersize=10, label=f'C1({c1[0]:.2f}, {c1[1]:.2f})')
ax.plot(c2[0], c2[1], 'go', markersize=10, label=f'C2({c2[0]:.2f}, {c2[1]:.2f})')
ax.plot(p[0], p[1], 'm*', markersize=15, label=f'P({p[0]:.2f}, {p[1]:.2f})')

ax.text(c1[0] + 0.2, c1[1] + 0.2, 'C1', fontsize=12, color='red', fontweight='bold')
ax.text(c2[0] + 0.2, c2[1] + 0.2, 'C2', fontsize=12, color='green', fontweight='bold')
ax.text(p[0] + 0.2, p[1] + 0.2, 'P', fontsize=12, color='magenta', fontweight='bold')

# Formatting
ax.set_title('Figure')
ax.grid(True)
ax.axis('equal')
ax.legend()
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/7.4.34/figs/figure1.png")
plt.show()
