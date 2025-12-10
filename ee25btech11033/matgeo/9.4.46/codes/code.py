
import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Part 1: Use the C function via a Shared Object ---

# Load the shared library

solver_lib = ctypes.CDLL('./code.so')

# Define the argument types for the C function
# void solve_quadratic(double a, double b, double c, double* root1, double* root2)
solver_lib.solve_quadratic.argtypes = [
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
# The function has a void return type, so restype is not needed.

# The equation from the document is x^2 - 7x - 60 = 0 
a, b, c = 1.0, -7.0, -60.0

# Create C-compatible double variables to store the results
root1 = ctypes.c_double()
root2 = ctypes.c_double()

# Call the C function, passing the variables by reference
solver_lib.solve_quadratic(a, b, c, ctypes.byref(root1), ctypes.byref(root2))

# Extract the Python float values from the C types
sol1 = root1.value
sol2 = root2.value

print(f"Roots found by C function: {sol1}, {sol2}")

# --- Part 2: Generate the First Plot (Parabola Intersection) ---

# Define the parabola
def parabola(x):
    return x**2 - 7*x - 60

x_vals = np.linspace(-10, 15, 400)
y_vals = parabola(x_vals)

plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, label=r'$y = x^2 - 7x - 60$')
plt.axhline(0, color='tab:orange')

# Plot the roots found by the C function
# Point A is the positive root, Point B is the negative root
plt.scatter(sol1, 0, s=100, facecolors='red', edgecolors='darkblue', linewidth=2, zorder=5)
plt.scatter(sol2, 0, s=90, marker='D', color='gold', zorder=5)

plt.annotate('A\n(12, 0)', xy=(sol1, 0), xytext=(sol1, 5), fontweight='bold', ha='center')
plt.annotate('B\n(-5, 0)', xy=(sol2, 0), xytext=(sol2, 5), fontweight='bold', ha='center')

plt.title('Intersection of $y = x^2 - 7x - 60$ with the x-axis')
plt.grid(True)
plt.legend(loc='lower left')
plt.xlim(-50, 50)
plt.ylim(-80, 30)
plt.show()


# --- Part 3: Generate the Second Plot (Circular Park) ---
# Substitute the C function's results into the logic from 'nativecode.py'

print("\nGenerating the circular park plot...")

# The length of a side cannot be negative, so we choose the positive root [cite: 63]
pa_dist = max(sol1, sol2)
# The difference between distances is 7m, so PB = PA - 7 [cite: 24]
pb_dist = pa_dist - 7

print(f"Using distances PA = {pa_dist}m and PB = {pb_dist}m for the plot.")

# The diameter of the circular park is 13 meters [cite: 6]
diameter = 13.0
radius = diameter / 2.0

# Gates A and B are diametrically opposite. We place them on the x-axis.
A = (-radius, 0)
B = (radius, 0)

# --- Calculations to find the coordinates of Pole P ---
# (This logic is preserved from nativecode.py)
px = (2 * radius**2 - pb_dist**2) / (2 * radius)
py = np.sqrt(radius**2 - px**2)
P = (px, py)

# --- Plotting the Figure ---
fig, ax = plt.subplots(figsize=(8, 8))

# 1. Plot the circular park boundary
park_circle = plt.Circle((0, 0), radius, color='green', fill=False, linestyle='--', linewidth=2, label='Park Boundary')
ax.add_patch(park_circle)

# 2. Plot the gates A, B and the pole P
ax.plot(A[0], A[1], 'ro', markersize=10, label='Gate A')
ax.plot(B[0], B[1], 'bo', markersize=10, label='Gate B')
ax.plot(P[0], P[1], 'kP', markersize=10, label='Pole P')

# 3. Draw the triangle APB
ax.plot([A[0], P[0]], [A[1], P[1]], 'k-')
ax.plot([B[0], P[0]], [B[1], P[1]], 'k-')
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', label=f'Diameter = {int(diameter)}m')

# 4. Annotate the points and distances
ax.text(A[0] - 0.5, A[1], 'A', fontsize=14, verticalalignment='center')
ax.text(B[0] + 0.5, B[1], 'B', fontsize=14, verticalalignment='center')
ax.text(P[0], P[1] + 0.5, 'P', fontsize=14, verticalalignment='center')

# Midpoints for distance labels
mid_AP = ((A[0] + P[0]) / 2, (A[1] + P[1]) / 2)
mid_BP = ((B[0] + P[0]) / 2, (B[1] + P[1]) / 2)
ax.text(mid_AP[0], mid_AP[1] - 0.5, f'{int(pa_dist)}m', color='blue', fontsize=12)
ax.text(mid_BP[0] + 0.5, mid_BP[1], f'{int(pb_dist)}m', color='blue', fontsize=12)

# 5. Show the right angle at P [cite: 12]
L = 0.5
x_vec_AP, y_vec_AP = A[0] - P[0], A[1] - P[1]
norm_AP = np.sqrt(x_vec_AP**2 + y_vec_AP**2)
x_vec_BP, y_vec_BP = B[0] - P[0], B[1] - P[1]
norm_BP = np.sqrt(x_vec_BP**2 + y_vec_BP**2)

p1 = (P[0] + L * x_vec_AP/norm_AP, P[1] + L * y_vec_AP/norm_AP)
p2 = (P[0] + L * x_vec_BP/norm_BP, P[1] + L * y_vec_BP/norm_BP)
p_corner = (p1[0] + p2[0] - P[0], p1[1] + p2[1] - P[1])
ax.plot([p1[0], p_corner[0], p2[0]], [p1[1], p_corner[1], p2[1]], 'k-')

# --- Final Plot Adjustments ---
ax.set_title('Position of Pole in a Circular Park', fontsize=16)
ax.set_xlabel('Distance (meters)')
ax.set_ylabel('Distance (meters)')
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':')
ax.legend()
ax.set_xlim(-radius - 2, radius + 2)
ax.set_ylim(-radius - 2, radius + 2)
plt.show()
