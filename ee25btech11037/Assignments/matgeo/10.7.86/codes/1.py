import matplotlib.pyplot as plt
import numpy as np

# --- Create Figure and Axis ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title("Locus of the Center of a Tangent Circle", fontsize=16)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_aspect('equal', adjustable='box') # This is crucial for circles to look like circles

# --- Define the Circles ---
# Circle C1 (large, outer circle)
center1 = (0, 0)
radius1 = 10.0

# Circle C2 (small, inner circle)
center2 = (3, 0)
radius2 = 2.0

center_c = (7.5, 0)
radius_c = 2.5

circle1 = plt.Circle(center1, radius1, color='blue', fill=False, lw=2, label='$C_1: x^2 + y^2 = 100$')
circle2 = plt.Circle(center2, radius2, color='red', fill=False, lw=2, label='$C_2: (x-3)^2 + y^2 = 4$')
circle_c = plt.Circle(center_c, radius_c, color='green', fill=False, lw=2, ls='--', label='C (Example)')

a = 6
b = np.sqrt(33.75)
ellipse_center_x = 1.5
t = np.linspace(0, 2 * np.pi, 200)
ellipse_x = ellipse_center_x + a * np.cos(t)
ellipse_y = b * np.sin(t)
locus_eq = r'Locus: $\sqrt{x^2 + y^2} + \sqrt{(x-3)^2 + y^2} = 12$'
ax.plot(ellipse_x, ellipse_y, color='purple', linestyle='-', label=locus_eq)


# --- Add Elements to the Plot ---
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle_c)

# Plot the center points
ax.plot(center1[0], center1[1], 'bo', label='Center of $C_1$ ($O_1$)')
ax.plot(center2[0], center2[1], 'ro', label='Center of $C_2$ ($O_2$)')
ax.plot(center_c[0], center_c[1], 'go', label='Center of C (O)')

# Add text labels with coordinates next to the centers
ax.text(center1[0] + 0.2, center1[1] + 0.2, f'$O_1 ({center1[0]}, {center1[1]})$', fontsize=12, color='blue')
ax.text(center2[0] + 0.2, center2[1] + 0.2, f'$O_2 ({center2[0]}, {center2[1]})$', fontsize=12, color='red')
ax.text(center_c[0] + 0.2, center_c[1] + 0.2, f'O ({center_c[0]}, {center_c[1]})$', fontsize=12, color='green')


# --- Set Plot Limits and Labels ---
# Adjust axes to fit all circles nicely.
ax.set_xlim(-11, 11)
ax.set_ylim(-11, 11)
ax.legend(loc='upper right')

# Display the plot
plt.savefig('1.png')
plt.show()


