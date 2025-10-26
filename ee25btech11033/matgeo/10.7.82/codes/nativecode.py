import matplotlib.pyplot as plt
import numpy as np

# --- Data from the PDF solution ---
C1_center = np.array([2., 1.])
C1_radius = 1.0
C2_center = np.array([6., 4.])
C2_radius = 4.0
P_contact = np.array([14/5, 8/5])

# --- Set up the plot ---
fig, ax = plt.subplots(figsize=(12, 9))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', alpha=0.6)

# --- Plot the two circles using trigonometric parameterization ---
# Generate a sequence of angles from 0 to 2*pi for a full circle.
# Increased points to 400 for a smoother curve.
theta = np.linspace(0, 2 * np.pi, 400) 

# Calculate x and y coordinates for Circle 1
x1 = C1_center[0] + C1_radius * np.cos(theta)
y1 = C1_center[1] + C1_radius * np.sin(theta)
ax.plot(x1, y1, color='blue', linewidth=2, label='Circle 1')

# Calculate x and y coordinates for Circle 2
x2 = C2_center[0] + C2_radius * np.cos(theta)
y2 = C2_center[1] + C2_radius * np.sin(theta)
ax.plot(x2, y2, color='green', linewidth=2, label='Circle 2')

# --- Plot the common tangents with separate colors ---
# Tangent 1 (y=0)
ax.axhline(0, color='red', linestyle='-', linewidth=2, label='Tangent: $y=0$')

# Tangent 2 (24x - 7y - 16 = 0)
x_vals = np.linspace(-1, 9, 400)
y_vals_tangent2 = (24 * x_vals - 16) / 7
ax.plot(x_vals, y_vals_tangent2, color='purple', linestyle='-', linewidth=2, label='Tangent: $24x-7y-16=0$')

# --- Plot and label important points ---
ax.plot(C1_center[0], C1_center[1], 'bo', markersize=5)
ax.text(C1_center[0] + 0.1, C1_center[1] + 0.1, '$C_1(2,1)$', fontsize=12)

ax.plot(C2_center[0], C2_center[1], 'go', markersize=5)
ax.text(C2_center[0] + 0.1, C2_center[1] + 0.1, '$C_2(6,4)$', fontsize=12)

ax.plot(P_contact[0], P_contact[1], 'ko', markersize=7)
ax.text(P_contact[0] + 0.1, P_contact[1] - 0.3, 'P (Point of Contact)', fontsize=12)

# --- Final plot formatting ---
ax.set_xlim(-1, 9)
ax.set_ylim(-2, 9)
ax.set_xlabel("X-axis", fontsize=12)
ax.set_ylabel("Y-axis", fontsize=12)
plt.title("Common Tangents of Two Touching Circles", fontsize=14)
plt.legend()
plt.tight_layout()


# To save the figure to a file
plt.savefig('../figs/fig.png')
