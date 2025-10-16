# Code revised for tangent construction
# October 4, 2025
# by Gemini
# released under GNU GPL
# Tangent to a Circle

import numpy as np
import matplotlib.pyplot as plt

# Helper function to generate points for a line segment
def line_gen(A, B):
    """Generates points for a line segment between A and B."""
    # Extend the line for better visualization by using a wider range
    len = 20
    x_AB = np.zeros((2, len))
    lam_1 = np.linspace(-0.5, 1.5, len) # Use a wider range to draw a longer line
    for i in range(len):
        temp1 = A + lam_1[i] * (B - A)
        x_AB[:, i] = temp1.flatten()
    return x_AB

# Helper function to generate points for a circle
def circ_gen(O, r):
    """Generates points for a circle with center O and radius r."""
    len = 100
    theta = np.linspace(0, 2 * np.pi, len)
    x_circ = np.zeros((2, len))
    x_circ[0, :] = r * np.cos(theta)
    x_circ[1, :] = r * np.sin(theta)
    x_circ = (x_circ.T + O.flatten()).T
    return x_circ

# 1. DEFINE CIRCLE AND EXTERNAL POINT
# Circle parameters
O = np.array([[0], [0]]) # Center at origin
r = 5                     # Radius 5cm

# External point P (8cm from the center)
P = np.array([[8], [0]])

# 2. CALCULATE TANGENT POINTS
# The points of contact lie on the polar line x = r^2 / P_x
x_contact = r**2 / P[0, 0]

# Find the y-coordinates by substituting x into the circle equation x^2 + y^2 = r^2
y_contact_sq = r**2 - x_contact**2
y_contact = np.sqrt(y_contact_sq)

# The two points of contact
T1 = np.array([[x_contact], [y_contact]])
T2 = np.array([[x_contact], [-y_contact]])

# 3. GENERATE GEOMETRIES FOR PLOTTING
# Generate the circle
x_circ = circ_gen(O, r)
# Generate the two tangent lines
x_tangent1 = line_gen(P, T1)
x_tangent2 = line_gen(P, T2)

# 4. PLOTTING
# Plot the tangent lines and the circle
plt.plot(x_tangent1[0, :], x_tangent1[1, :], label='Tangent 1')
plt.plot(x_tangent2[0, :], x_tangent2[1, :], label='Tangent 2')
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle')

# Plot the polar line
plt.axvline(x=x_contact, color='r', linestyle='--', label=f'Polar Line (x={x_contact:.2f})')

# Plot and label the key points
points = {'O (Center)': O, 'P (External Pt)': P, 'T1': T1, 'T2': T2}
for label, point in points.items():
    plt.scatter(point[0], point[1])
    plt.annotate(f'{label}\n({point[0,0]:.2f}, {point[1,0]:.2f})',
                 (point[0,0], point[1,0]),
                 textcoords="offset points",
                 xytext=(10,5),
                 ha='left')

# --- NEW: Add equation labels to the plot ---
plt.text(0, 3, r'$x^2 + y^2 = 25$', fontsize=12, color='blue', ha='center')
plt.text(5.5, 2.5, r'$5x - \sqrt{39}y - 40 = 0$', fontsize=12, color='green', rotation=-32)
plt.text(5.5, -2.5, r'$5x + \sqrt{39}y - 40 = 0$', fontsize=12, color='purple', rotation=32)
# ---------------------------------------------

# Set plot properties
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.title('Construction of Tangents to a Circle')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
