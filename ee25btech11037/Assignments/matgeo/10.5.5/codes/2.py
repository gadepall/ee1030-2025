import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define Geometry and Perform Calculations ---

# Define the radii for the two concentric circles
r_small = 4.0
r_large = 6.0

# The center of the circles is at the origin
O = np.array([0, 0])

# Place point P on the edge of the large circle (e.g., on the x-axis)
P = np.array([r_large, 0])

PO_length = r_large
TO_length = r_small

# Calculate the length of the tangent PT using the Pythagorean theorem
PT_length = np.sqrt(PO_length**2 - TO_length**2)

# Calculate the angle POT (let's call it alpha) to find the coordinates of T
# In the right triangle OPT, cos(alpha) = adjacent/hypotenuse = TO/PO
alpha = np.arccos(TO_length / PO_length)

# The coordinates of the tangent point T on the small circle
T = np.array([r_small * np.cos(alpha), r_small * np.sin(alpha)])


# Generate points to draw the circles
theta_vals = np.linspace(0, 2 * np.pi, 400)
x_small_circle = r_small * np.cos(theta_vals)
y_small_circle = r_small * np.sin(theta_vals)
x_large_circle = r_large * np.cos(theta_vals)
y_large_circle = r_large * np.sin(theta_vals)


# --- 3. Create the Plot ---

# Set up the figure
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the two circles
ax.plot(x_small_circle, y_small_circle, 'b-', label=f'Smaller Circle (r={r_small})')
ax.plot(x_large_circle, y_large_circle, 'g-', label=f'Larger Circle (r={r_large})')

# Plot the lines of the triangle OPT
ax.plot([P[0], T[0]], [P[1], T[1]], 'r-', linewidth=2.5, label='Tangent PT')
ax.plot([O[0], P[0]], [O[1], P[1]], 'k--', label='Line PO (Hypotenuse)')
ax.plot([O[0], T[0]], [O[1], T[1]], 'k--', label='Line TO (Radius)')

# Plot and label the points O, P, and T
ax.scatter(*O, color='black', zorder=5)
ax.text(O[0] - 0.3, O[1] - 0.3, 'O', fontsize=14, weight='bold')

ax.scatter(*P, color='red', s=50, zorder=5)
ax.text(P[0] + 0.1, P[1] - 0.1, 'P', fontsize=14, color='red')

ax.scatter(*T, color='blue', s=50, zorder=5)
ax.text(T[0] + 0.2, T[1] + 0.2, 'T', fontsize=14, color='blue')

# Add labels for the lengths of the triangle sides
ax.text((P[0] + T[0]) / 2, (P[1] + T[1]) / 2 + 0.2, f"PT = {PT_length:.2f}", fontsize=12, color='red')
ax.text(PO_length / 2, -0.5, f"PO = {PO_length}", fontsize=12, color='black')
ax.text(T[0] / 2 + 0.2, T[1] / 2, f"TO = {TO_length}", fontsize=12, color='blue')

# --- 4. Finalize and Show Plot ---

# Set aspect ratio to be equal, so circles are not distorted
ax.set_aspect('equal', adjustable='box')

# Add title and legend
ax.set_title("Tangent from a Point on a Concentric Circle", fontsize=16)
ax.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.savefig('2.png')
plt.show()

