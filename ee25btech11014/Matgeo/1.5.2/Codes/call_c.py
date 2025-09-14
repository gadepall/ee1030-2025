import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# Load compiled C library
c_lib = ctypes.CDLL('./code.so')

# Define C function signature:
# sec_form(x1, y1, x2, y2, m*, n*, px*, py*)
c_lib.sec_form.argtypes = [
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)
]
c_lib.sec_form.restype = None  # void

# Define points A and B
A = np.array([6, -4], dtype=float)
B = np.array([-2, -7], dtype=float)

# Prepare variables for C outputs
m = ctypes.c_int()
n = ctypes.c_int()
px = ctypes.c_float()
py = ctypes.c_float()

# Call C function
c_lib.sec_form(int(A[0]), int(A[1]), int(B[0]), int(B[1]),
               ctypes.byref(m), ctypes.byref(n),
               ctypes.byref(px), ctypes.byref(py))

# Extract results from C
P_dividing = np.array([px.value, py.value])
ratio = (m.value, n.value)

print(f"The Y-axis divides the line in the ratio {ratio[0]}:{ratio[1]}")
print(f"Intersection Point: {tuple(P_dividing)}")

# --- Plotting ---
def generate_line_segment(point1, point2, num_points=50):
    """Generate points on the line segment between point1 and point2."""
    line_segment = np.zeros((2, num_points))
    lambda_vals = np.linspace(0, 1, num_points)
    for i in range(num_points):
        temp = point1 + lambda_vals[i] * (point2 - point1)
        line_segment[:, i] = temp.T
    return line_segment

# Generate line segment for plotting
x_AB = generate_line_segment(A, B)

plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')

# Plot points A, B, and P
all_points = np.vstack((A, B, P_dividing)).T
plt.scatter(all_points[0, :], all_points[1, :], color='red')

# Add labels
point_labels = [f'A {tuple(A)}', f'B {tuple(B)}', f'P {tuple(P_dividing)}']
offsets = [(10, 5), (-30, -10), (15, -15)]
for i, txt in enumerate(point_labels):
    plt.annotate(txt,
                 (all_points[0, i], all_points[1, i]),
                 textcoords="offset points",
                 xytext=offsets[i],
                 ha='center')

# Set plot details
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(f'Point P{tuple(P_dividing)} divides AB in ratio {ratio[0]}:{ratio[1]}')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

# Save and show plot
plt.savefig('../Figs/graph.png')
plt.show()
