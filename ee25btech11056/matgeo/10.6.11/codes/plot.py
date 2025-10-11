import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..", "figs")

# Input: Circle of radius r, center at origin
r = 4.0
Px, Py = 8.0, 0.0  # External point P(8,0)

# Tangent points (from previous C output)
T1 = (2.0, 3.4641)
T2 = (2.0, -3.4641)

# Circle points using x^2 + y^2 = r^2
x_vals = np.linspace(-r, r, 500)  # x in [-r, r]
y_upper = np.sqrt(r**2 - x_vals**2)
y_lower = -np.sqrt(r**2 - x_vals**2)

# Center
Ox, Oy = 0.0, 0.0

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))

# Plot circle (upper and lower halves)
ax.plot(x_vals, y_upper, 'g', label="Circle: $x^2+y^2=16$")
ax.plot(x_vals, y_lower, 'g')

# Plot external point P and center O
ax.scatter(Px, Py, color="blue")
ax.text(Px + 0.2, Py, f"P({Px:.0f},{Py:.0f})", fontsize=10, color="blue")
ax.scatter(Ox, Oy, color="black")
ax.text(Ox - 0.5, Oy - 0.3, "O(0,0)", fontsize=10, color="black")

# Plot tangent points
ax.scatter(*T1, color="red")
ax.text(T1[0] + 0.2, T1[1] + 0.2, f"q1({T1[0]:.2f},{T1[1]:.2f})", fontsize=10, color="red")
ax.scatter(*T2, color="red")
ax.text(T2[0] + 0.2, T2[1] - 0.3, f"q2({T2[0]:.2f},{T2[1]:.2f})", fontsize=10, color="red")

# Draw tangents PT1 and PT2
ax.plot([Px, T1[0]], [Py, T1[1]], 'm', label="Tangent 1")
ax.plot([Px, T2[0]], [Py, T2[1]], 'm', label="Tangent 2")

# Mark the angle at P as 60 degrees
ax.text(Px - 1.5, Py, r"$60^\circ$", fontsize=12, color="purple")

# Axes at center
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# Formatting
ax.set_aspect("equal")
ax.set_xlim(-5, 10)
ax.set_ylim(-6, 6)
ax.legend()
ax.set_title("Tangents from External Point to Circle")
ax.grid(True)

# Save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "circle_tangents.png"))
plt.show()

