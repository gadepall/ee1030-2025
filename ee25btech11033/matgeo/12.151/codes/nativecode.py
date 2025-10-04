import matplotlib.pyplot as plt
import numpy as np


# A point on the Mohr's circle, P 
p_coords = (10, 3)
# The center of the Mohr's circle, C 
center_coords = (6, 0)
# The point diametrically opposite to P, P' [cite: 19], with coordinates from the solution [cite: 28]
p_prime_coords = (2, -3)

# --- Calculations for plotting ---
# The radius is the distance from the center to any point on the circle (e.g., P)
radius = np.sqrt((p_coords[0] - center_coords[0])**2 + (p_coords[1] - center_coords[1])**2)

# --- Plotting Setup ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box') # Ensure the circle is not distorted

# --- Draw the Mohr's Circle ---
# Create a circle object and add it to the plot
mohr_circle = plt.Circle(center_coords, radius, color='skyblue', fill=False, linewidth=2, label="Mohr's Circle")
ax.add_patch(mohr_circle)

# --- Plot the points C, P, and P' ---
# Center C
ax.plot(center_coords[0], center_coords[1], 'ro', markersize=8, label='Center C')
# Point P
ax.plot(p_coords[0], p_coords[1], 'go', markersize=8, label='Point P')
# Point P'
ax.plot(p_prime_coords[0], p_prime_coords[1], 'mo', markersize=8, label="Point P'")

# --- Draw the diameter connecting P and P' ---
ax.plot([p_coords[0], p_prime_coords[0]], [p_coords[1], p_prime_coords[1]], 'k--', label="Diameter P-P'")

# --- Annotations: Mark the points near them ---
# Add text labels with a slight offset for clarity
ax.text(center_coords[0] + 0.2, center_coords[1] - 0.5, f'C{center_coords}', fontsize=12, color='red')
ax.text(p_coords[0] + 0.2, p_coords[1] + 0.2, f'P{p_coords}', fontsize=12, color='green')
ax.text(p_prime_coords[0] + 0.2, p_prime_coords[1] - 0.2, f"P'{p_prime_coords}", fontsize=12, color='purple')

# --- Formatting the plot ---
# Set axis labels based on the problem description [cite: 15]
ax.set_xlabel('Normal Stress (σ) [MPa]', fontsize=12)
ax.set_ylabel('Shear Stress (τ) [MPa]', fontsize=12)
ax.set_title("Mohr's Circle for Stress State", fontsize=14)

# Set axis limits to give some padding around the circle
ax.set_xlim(0, 12)
ax.set_ylim(-6, 6)

# Add grid and move axes to pass through (0,0)
ax.grid(True, linestyle=':')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.legend()
plt.savefig('../figs/fig.png')
plt.show()
