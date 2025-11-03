import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# --- 1. Setup the figure and axis ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', alpha=0.6)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# --- 2. Define and plot the original circle (C) ---
r_C = 3
theta = np.linspace(0, 2 * np.pi, 200)
x_C = r_C * np.cos(theta)
y_C = r_C * np.sin(theta)
ax.plot(x_C, y_C, 'b-', label=r'Original Circle C: $x^2 + y^2 = 9$')

# --- 3. Define and plot the locus of midpoints ---
# The distance of the midpoint from the center is r_C * cos((2pi/3)/2) = 3 * cos(pi/3) = 1.5
r_locus = 1.5
x_locus = r_locus * np.cos(theta)
y_locus = r_locus * np.sin(theta)
ax.plot(x_locus, y_locus, 'r--', label=r'Locus of Midpoints: $x^2 + y^2 = \frac{9}{4}$')

# --- 4. Draw an example chord and radii to illustrate ---
# Angle of the radius to the chord midpoint
angle_midpoint = np.pi / 4

# Center
O = (0, 0)
# Midpoint P
P = (r_locus * np.cos(angle_midpoint), r_locus * np.sin(angle_midpoint))
# Endpoints of the chord (A and B)
angle_subtended_half = np.pi / 3  # Half of 2pi/3
A = (r_C * np.cos(angle_midpoint + angle_subtended_half), r_C * np.sin(angle_midpoint + angle_subtended_half))
B = (r_C * np.cos(angle_midpoint - angle_subtended_half), r_C * np.sin(angle_midpoint - angle_subtended_half))

# Plot the illustrative elements
ax.plot([A[0], B[0]], [A[1], B[1]], 'g-', label=r'Example Chord subtending $\frac{2\pi}{3}$') # Chord AB
ax.plot([O[0], A[0]], [O[1], A[1]], 'k:', alpha=0.8) # Radius OA
ax.plot([O[0], B[0]], [O[1], B[1]], 'k:', alpha=0.8) # Radius OB
ax.plot([O[0], P[0]], [O[1], P[1]], 'm-', alpha=0.8) # Line to midpoint OP

# Plot and label the points
ax.plot(O[0], O[1], 'ko')
ax.text(O[0] - 0.2, O[1] - 0.2, 'O', fontsize=12)
ax.plot(P[0], P[1], 'mo')
ax.text(P[0] + 0.1, P[1] + 0.1, 'P (midpoint)', fontsize=12, color='m')

# Add angle annotation
angle_rad = 2 * np.pi / 3
arc = Arc(O, 2, 2, angle=0,
          theta1=np.degrees(angle_midpoint - angle_subtended_half),
          theta2=np.degrees(angle_midpoint + angle_subtended_half),
          color='purple', lw=1.5, linestyle='-')
ax.add_patch(arc)
angle_text_pos = (0.8 * np.cos(angle_midpoint), 0.8 * np.sin(angle_midpoint))
ax.text(angle_text_pos[0], angle_text_pos[1], r'$\frac{2\pi}{3}$', fontsize=14, color='purple', ha='center', va='center')


# --- 5. Finalize and show the plot ---
ax.set_title('Locus of the Midpoints of Chords', fontsize=16)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.legend()
plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)
plt.show()