import ctypes

import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (optional)
lib = ctypes.CDLL('./mat.so')
lib.find_pts.argtypes = [ctypes.c_int]
lib.find_pts.restype = None

# Circle parameters
r = np.sqrt(6)                     # radius
center = np.array([0, np.sqrt(2)]) # center (0, sqrt(2))

# Rational points (no int truncation!)
x_val = round(np.sqrt(r**2 - 2), 6)
points = [(x_val, 0), (-x_val, 0)]

# Call the C function for consistency
print("From C function:")
lib.find_pts(int(round(r**2)))

# Circle coordinates
theta = np.linspace(0, 2*np.pi, 500)
x_circle = center[0] + r * np.cos(theta)
y_circle = center[1] + r * np.sin(theta)

# Plot
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x_circle, y_circle, label="Circle")

# Mark rational points P1 and P2
labels = ["P1", "P2"]
for i, (px, py) in enumerate(points):
    ax.scatter(px, py, color="red", s=90, zorder=5)
    ax.text(px + 0.2, py - 0.3, f"{labels[i]} ({px:.0f},{py:.0f})",
            color="red", fontsize=11, weight="bold")

# Mark the center
ax.scatter(center[0], center[1], color="blue", s=80)
ax.text(center[0] + 0.1, center[1] + 0.1, "Center (0,√2)",
        color="blue", fontsize=11)

# Add equation of the circle
circle_eq = r"$(x-0)^2 + (y-\sqrt{2})^2 = 6$"
ax.text(-4.8, 4.5, circle_eq, fontsize=12, color="purple",
        bbox=dict(facecolor="white", alpha=0.6))

# Draw radius lines from center to P1 and P2
for (px, py) in points:
    ax.plot([center[0], px], [center[1], py], linestyle="--", color="gray")

# Larger meshgrid and axes
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.6)

plt.savefig('1.png')
plt.show()

