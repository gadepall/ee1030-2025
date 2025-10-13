import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mat.so')
c_library = ctypes.CDLL(lib_path)

# Define the function's argument and return types
c_function = c_library.calculateOALength
c_function.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
c_function.restype = ctypes.c_double

# Problem parameters: radius=3, tangents y=x (m1=[1,1]) and y=2x (m2=[1,2])
radius = 3.0
m1 = (1.0, 1.0)
m2 = (1.0, 2.0)

# Call the C function to get the length of OA
oa_length = c_function(radius, m1[0], m1[1], m2[0], m2[1])

print(f"Length of OA = {oa_length:.4f}\n")

# Plot the tangent lines y=x and y=2x
x_range = np.linspace(-1, 15, 100)
y_tangent1 = 1 * x_range
y_tangent2 = 2 * x_range

# Geometrically place the points for plotting
# Point A (Point of Contact) is on y=x at a distance of oa_length from origin
poc_A = np.array([oa_length / np.sqrt(2), oa_length / np.sqrt(2)])

# Circle Center C is on the normal to y=x at A, at a distance of 'radius'
# Normal direction to y=x is (-1, 1)
normal_dir = np.array([-1, 1]) / np.sqrt(2)
center_C = poc_A + radius * normal_dir

# --- Create the Plot ---
fig, ax = plt.subplots(figsize=(12, 10))

# Plot the circle
circle = plt.Circle(center_C, radius, color='skyblue', fill=False, lw=2, label=f'Circle (r={radius})')
ax.add_patch(circle)

# Plot tangents
ax.plot(x_range, y_tangent1, 'g-', label='Tangent y=x')
ax.plot(x_range, y_tangent2, 'orange', linestyle='--', label='Tangent y=2x')

# Plot the triangle OAC
ax.plot([0, poc_A[0]], [0, poc_A[1]], 'r-', label=f'OA (length={oa_length:.2f})')
ax.plot([poc_A[0], center_C[0]], [poc_A[1], center_C[1]], 'm-', label=f'AC (radius={radius})')
ax.plot([0, center_C[0]], [0, center_C[1]], 'k:', label='Line OC (Angle Bisector)')

# Plot and label key points
ax.plot(0, 0, 'ko', markersize=8, label='Origin O')
ax.plot(poc_A[0], poc_A[1], 'ro', markersize=8, label='Point of Contact A')
ax.plot(center_C[0], center_C[1], 'bo', markersize=8, label='Center C')

# Add annotations
ax.text(poc_A[0] - 1.5, poc_A[1] + 1.5, f'A({poc_A[0]:.1f}, {poc_A[1]:.1f})', color='red')
ax.text(center_C[0] + 0.5, center_C[1], f'C({center_C[0]:.1f}, {center_C[1]:.1f})', color='blue')

# Formatting
ax.set_title('Visualization for Problem 10.7.84', fontsize=16)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.grid(True, linestyle=':')
ax.legend(loc='upper left')
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-2, 18)
ax.set_ylim(-2, 18)

plt.savefig('1.png')
plt.show()