import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
a = 2
b = 1

# --- Circle Properties ---
center = (a/2, b/4)
radius = np.sqrt(a**2/4 + b**2/16)

# --- External Point ---
P = (a, b/2)

# --- Find Chord Midpoints (on x-axis) ---
# Roots of 8h^2 - 12ah + (4a^2 + b^2) = 0
h_coeffs = [8, -12*a, 4*a**2 + b**2]
h_roots = np.roots(h_coeffs)
M1 = (h_roots[0], 0)
M2 = (h_roots[1], 0)

# --- Find Chord Endpoints Q (on the circle) ---
# The y-coordinate of the other endpoint Q must be -b/2
# The x-coordinates are roots of 2x^2 - 2ax + b^2 = 0
x_coeffs = [2, -2*a, b**2]
x_roots = np.roots(x_coeffs)
Q1 = (x_roots[0], -b/2)
Q2 = (x_roots[1], -b/2)

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the circle
circle_patch = plt.Circle(center, radius, color='skyblue', fill=False, lw=2)
ax.add_patch(circle_patch)

# Plot the chords
ax.plot([P[0], Q1[0]], [P[1], Q1[1]], 'r-')
ax.plot([P[0], Q2[0]], [P[1], Q2[1]], 'g-')

# Plot the key points
ax.plot(*P, 'ko', markersize=8)
ax.plot(*center, 'bo', markersize=8)
ax.plot(*M1, 'ro', markersize=6)
ax.plot(*M2, 'go', markersize=6)

# Plot the x-axis
ax.axhline(0, color='black', lw=2)

# --- Direct Annotation on the Graph ---
# Use ax.text() to add labels next to the points
ax.text(P[0] + 0.05, P[1], f' P({P[0]:.1f}, {P[1]:.1f})', verticalalignment='center')
ax.text(center[0] - 0.05, center[1] - 0.1, f'C({center[0]:.1f}, {center[1]:.2f})', horizontalalignment='right')
ax.text(M1[0], M1[1] + 0.05, f'M1 ({M1[0]:.2f},0)', horizontalalignment='center')
ax.text(M2[0], M2[1] + 0.05, f'M2 ({M2[0]:.2f},0)', horizontalalignment='center')
ax.text(-0.25, 0.05, 'X-axis (bisector)')

# --- Formatting ---
ax.set_aspect('equal', adjustable='box')
ax.set_title('For a = 2 and b = 1', fontsize=16)
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
plt.grid(True)
plt.savefig('../figs/fig.png')
plt.show()
