
import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# Load compiled C library
c_lib = ctypes.CDLL('./code.so')

# Define C function signature: takes 5 floats, returns float
# (Ax, Ay, Bx, By, Px) and returns Py
c_lib.findM.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float,
                        ctypes.c_float, ctypes.c_float]
c_lib.findM.restype = ctypes.c_float

# Define points A and B
A = np.array([6.0, -4.0])
B = np.array([-2.0, -7.0])
Px = 0.0  # x = 0 (Y-axis)

# Call C function to get Py (y-coordinate of intersection with Y-axis)
Py = c_lib.findM(
    ctypes.c_float(A[0]),
    ctypes.c_float(A[1]),
    ctypes.c_float(B[0]),
    ctypes.c_float(B[1]),
    ctypes.c_float(Px)
)

# The dividing point on the Y-axis
P_dividing = np.array([Px, Py])

def find_ratio(point_A, point_B, dividing_point):
    A_vec = np.array(point_A)
    B_vec = np.array(point_B)
    P_vec = np.array(dividing_point)

    epsilon = 1e-9
    ratio_vector = (P_vec - A_vec) / (B_vec - P_vec + epsilon)
    return ratio_vector

# Calculate and print the ratio
ratio = find_ratio(A, B, P_dividing)
print(f'Point {tuple(P_dividing)} divides the line AB in the ratio: {round(ratio[0])}:{round(ratio[1])}')

def generate_line_segment(point1, point2, num_points=10):
    dim = point1.shape[0]
    line_segment = np.zeros((dim, num_points))
    lambda_vals = np.linspace(0, 1, num_points)
    for i in range(num_points):
        temp = point1 + lambda_vals[i] * (point2 - point1)
        line_segment[:, i] = temp.T
    return line_segment

# Generate line segment for plotting
x_AB = generate_line_segment(A, B)

# Plotting
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')

# Plot points A, B, and P
all_points = np.vstack((A, B, P_dividing)).T
plt.scatter(all_points[0, :], all_points[1, :], color='red')

# Add labels
point_labels = [f'A {tuple(A)}', f'B {tuple(B)}', f'P {tuple(P_dividing)}']
for i, txt in enumerate(point_labels):
    plt.annotate(txt,
                 (all_points[0, i], all_points[1, i]),
                 textcoords="offset points",
                 xytext=(10, 5),
                 ha='center')

# Set plot details
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(f'Point P{tuple(P_dividing)} divides AB in ratio of {round(ratio[0])}:{round(ratio[1])}')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

# Save and show plot
plt.savefig('../Figs/graph3d.png')
plt.show()
