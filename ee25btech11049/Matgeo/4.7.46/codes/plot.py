import numpy as np
import matplotlib.pyplot as plt
from libs.funcs import line_dir_pt
from libs.params import omat # Import the rotation matrix

# --- Mathematical Setup ---
# The equation of a line is n.T * x = p.
# We are given a point P(1, 0) on the line and distance from origin d = sqrt(3)/2.
# From the derivation, we found the relationship a^2 = 3*b^2 for the normal vector n = [a, b].T.
# We choose a=sqrt(3), which gives b = +/-1.
n1 = np.array([np.sqrt(3), 1]).reshape(-1, 1)
n2 = np.array([np.sqrt(3), -1]).reshape(-1, 1)

# The point through which the lines pass
P = np.array([1, 0]).reshape(-1, 1)
O = np.array([0, 0]).reshape(-1, 1)
d = np.sqrt(3)/2

# --- Line Generation ---
# The direction vector 'm' of a line is perpendicular to its normal vector 'n'.
# We find 'm' by rotating 'n' by 90 degrees using the 'omat' matrix.
m1 = omat @ n1
m2 = omat @ n2

# Generate points for the two lines using the direction vector and the point P.
line1 = line_dir_pt(m1, P, k1=-2, k2=2)
line2 = line_dir_pt(m2, P, k1=-2, k2=2)

# --- Plotting ---
plt.figure(figsize=(8, 8))

# Plot the two lines
plt.plot(line1[0, :], line1[1, :], label=r'$\sqrt{3}x + y - \sqrt{3} = 0$')
plt.plot(line2[0, :], line2[1, :], label=r'$\sqrt{3}x - y - \sqrt{3} = 0$')

# Plot the point P and the Origin O
plt.plot(P[0], P[1], 'o', color='red', markersize=8, label='Point P(1, 0)')
plt.plot(O[0], O[1], 'o', color='black', markersize=8, label='Origin O(0, 0)')

# To verify the distance, plot a circle with radius d centered at the origin.
# The lines should appear tangent to this circle.
circle = plt.Circle((0, 0), d, color='gray', linestyle='--', fill=False, label=f'Distance d ≈ {d:.2f}')
plt.gca().add_artist(circle)

# --- Plot Customization ---
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title(r"Lines through (1, 0) at a distance of $\frac{\sqrt{3}}{2}$ from the Origin")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.axis('equal') # Ensures correct aspect ratio
plt.xlim(-1.5, 2.5)
plt.ylim(-2, 2)
plt.show()
