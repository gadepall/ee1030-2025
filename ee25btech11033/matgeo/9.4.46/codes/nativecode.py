import matplotlib.pyplot as plt
import numpy as np

# --- Problem Data based on the PDF ---
# The diameter of the circular park is 13 meters.
diameter = 13
radius = diameter / 2.0

# Gates A and B are diametrically opposite. We can place them on the x-axis.
A = (-radius, 0)
B = (radius, 0)

# The distances of the pole P from gates A and B are 12m and 5m respectively.
# The source document has a typo "PB=12 and PB=5".
# Based on the equations PA+PB=17 and PA-PB=7, the correct values are PA=12 and PB=5.
pa_dist = 12
pb_dist = 5

# --- Calculations to find the coordinates of Pole P ---
# Let P = (x, y). P lies on the circle x^2 + y^2 = radius^2.
# Using the distance formula from P to B: (x - radius)^2 + y^2 = pb_dist^2
# x^2 - 2*x*radius + radius^2 + y^2 = pb_dist^2
# Since x^2 + y^2 = radius^2, we substitute it in:
# radius^2 - 2*x*radius + radius^2 = pb_dist^2
# 2*radius^2 - 2*x*radius = pb_dist^2
# 2*x*radius = 2*radius^2 - pb_dist^2
# x = (2*radius**2 - pb_dist**2) / (2*radius)
px = (2 * radius**2 - pb_dist**2) / (2 * radius)

# Find y from the circle equation: y^2 = radius^2 - x^2
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
ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', label=f'Diameter = {diameter}m')

# 4. Annotate the points and distances
ax.text(A[0] - 1, A[1], 'A', fontsize=14, verticalalignment='center')
ax.text(B[0] + 0.5, B[1], 'B', fontsize=14, verticalalignment='center')
ax.text(P[0], P[1] + 0.5, 'P', fontsize=14, verticalalignment='center')

# Midpoints for distance labels
mid_AP = ((A[0] + P[0]) / 2, (A[1] + P[1]) / 2)
mid_BP = ((B[0] + P[0]) / 2, (B[1] + P[1]) / 2)
ax.text(mid_AP[0], mid_AP[1] - 0.5, f'{pa_dist}m', color='blue', fontsize=12)
ax.text(mid_BP[0] + 0.5, mid_BP[1], f'{pb_dist}m', color='blue', fontsize=12)

# 5. Show the right angle at P
# As described in the PDF, the angle at P is 90 degrees 
L = 0.5 # size of the right-angle symbol
x_vec_AP = A[0] - P[0]
y_vec_AP = A[1] - P[1]
norm_AP = np.sqrt(x_vec_AP**2 + y_vec_AP**2)
x_vec_BP = B[0] - P[0]
y_vec_BP = B[1] - P[1]
norm_BP = np.sqrt(x_vec_BP**2 + y_vec_BP**2)

# Points for the right-angle symbol
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

# Set axis limits to give some padding around the circle
ax.set_xlim(-radius - 2, radius + 2)
ax.set_ylim(-radius - 2, radius + 2)
plt.savefig('../figs/fig.png')
plt.show()
