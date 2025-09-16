
import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL('./code.so')
except OSError:
    print("Error: 'code.so' not found.")
    print("Please compile code.c using: gcc -shared -o code.so -fPIC code.c")
    exit()

# Define argument and return types for the C function
c_lib.find_ratio.argtypes = [
    ctypes.c_float, ctypes.c_float,  # Ax, Ay
    ctypes.c_float, ctypes.c_float   # Bx, By
]
c_lib.find_ratio.restype = ctypes.c_float

# --- Points ---
A = np.array([3.0, 6.0])
B = np.array([-12.0, -3.0])

# --- Call C function to compute ratio ---
ratio = c_lib.find_ratio(
    ctypes.c_float(A[0]), ctypes.c_float(A[1]),
    ctypes.c_float(B[0]), ctypes.c_float(B[1])
)

print(f"✅ The X-axis divides AB in the ratio {ratio:.2f}:1")

# --- Geometry in Python ---
# Equation of line AB: y = slope*x + intercept
slope = (B[1] - A[1]) / (B[0] - A[0])
intercept = A[1] - slope * A[0]

# Intersection with X-axis (y=0)
x_intersect = -intercept / slope
X = np.array([x_intersect, 0.0])

# Distances AX and XB
AX = np.linalg.norm(A - X)
XB = np.linalg.norm(B - X)

print(f"Point X is at ({X[0]:.2f}, 0)")
print(f"Ratio AX:XB = {AX:.0f}:{XB:.0f}")

# --- Plotting ---
x_min = min(A[0], B[0], X[0]) - 2
x_max = max(A[0], B[0], X[0]) + 2
x_line = np.linspace(x_min, x_max, 100)
y_line = slope * x_line + intercept

plt.plot(x_line, y_line, label='Line AB', color='blue')

# Scatter points A, B, and X
all_points = np.vstack((A, B, X)).T
plt.scatter(
    all_points[0, :],
    all_points[1, :],
    color=['red', 'green', 'purple'],
    zorder=5
)

# Labels for points
point_labels = [
    f'A({A[0]},{A[1]})',
    f'B({B[0]},{B[1]})',
    f'X({X[0]:.1f},0)'
]

for i, txt in enumerate(point_labels):
    plt.annotate(
        txt,
        (all_points[0, i], all_points[1, i]),
        textcoords="offset points",
        xytext=(10, 5),
        ha='center'
    )

# Axes, labels, and grid
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('X-axis dividing line segment AB')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')
plt.show()