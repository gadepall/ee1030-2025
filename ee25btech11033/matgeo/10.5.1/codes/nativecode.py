import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# --- Define all the geometric points and circle parameters from the solution ---
A = np.array([0, 6])
B = np.array([0, 0])
C = np.array([8, 0])
D = np.array([72/25, 96/25])  # Foot of the perpendicular from B to AC

# Circle properties
circle_center = np.array([4, 0])
radius = 4.0

# Tangent point T2 (T1 is at B)
T2 = np.array([72/13, 48/13])

# --- Set up the plot ---
fig, ax = plt.subplots(figsize=(12, 9))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', alpha=0.7)

# --- Plot the Triangle ABC ---
# Plot vertices and edges
ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-', label='Triangle ABC', linewidth=2)

# --- Plot the complete Circle ---
# The patches.Circle function already draws the full circle.
circle = patches.Circle(circle_center, radius, edgecolor='red', facecolor='none', linewidth=2, label='Circle through B, C, D')
ax.add_patch(circle)

# --- Plot the Altitude BD ---
ax.plot([B[0], D[0]], [B[1], D[1]], 'g--', label='Altitude BD')

# --- Plot the Tangent Lines from point A with the same color ---
TANGENT_COLOR = 'purple'

# Tangent 1 is the y-axis (line x=0)
ax.axvline(0, color=TANGENT_COLOR, linestyle='-', linewidth=2.5, label='Tangent 1: x=0')

# Tangent 2 is the line 5x + 12y = 72
x_vals = np.linspace(-1, 10, 400)
y_vals_tangent = (72 - 5 * x_vals) / 12
ax.plot(x_vals, y_vals_tangent, color=TANGENT_COLOR, linestyle='-', linewidth=2, label='Tangent 2: 5x+12y=72')

# --- Plot and mark the specified points ---
# This dictionary now only contains the points to be labeled.
points_to_mark = {'A': A, 'B': B, 'C': C, 'D': D, '$T_2$': T2}

# Plot the circle center as a dot without a label
ax.plot(circle_center[0], circle_center[1], 'ko', markersize=6)

# Plot and label the specified points
for label, p in points_to_mark.items():
    ax.plot(p[0], p[1], 'ko', markersize=6)
    # Add text labels with a small offset for clarity
    ax.text(p[0] + 0.15, p[1] + 0.15, label, fontsize=12, verticalalignment='bottom')

# --- Final plot formatting ---
ax.set_xlabel("X-axis", fontsize=12)
ax.set_ylabel("Y-axis", fontsize=12)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-2, 10)
ax.set_ylim(-2, 8)
plt.legend(loc='upper right')
plt.tight_layout()



# Or to save the plot to a file
plt.savefig('../figs/fig.png')
