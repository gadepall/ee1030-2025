import numpy as np
import matplotlib.pyplot as plt

# Circle parameters
r = np.sqrt(6)                     # radius
center = np.array([0, np.sqrt(2)]) # center (0, √2)

# Rational points
x_val = round(np.sqrt(r**2 - 2), 6)   # should be 2.0
points = [(x_val, 0), (-x_val, 0)]

# Generate circle coordinates
theta = np.linspace(0, 2*np.pi, 500)
x_circle = center[0] + r * np.cos(theta)
y_circle = center[1] + r * np.sin(theta)

# Plot setup
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x_circle, y_circle, label="Circle")

# Mark rational points P1 and P2
labels = ["P1", "P2"]
for i, (px, py) in enumerate(points):
    ax.scatter(px, py, color="red", s=90, zorder=5)
    ax.text(px + 0.2, py - 0.3, f"{labels[i]} ({px:.0f},{py:.0f})",
            color="red", fontsize=11, weight="bold")
    # Draw radius lines
    ax.plot([center[0], px], [center[1], py], linestyle="--", color="gray")

# Mark the center
ax.scatter(center[0], center[1], color="blue", s=80)
ax.text(center[0] + 0.1, center[1] + 0.1, "Center (0,√2)",
        color="blue", fontsize=11)

# Add circle equation on plot
circle_eq = r"$(x-0)^2 + (y-\sqrt{2})^2 = 6$"
ax.text(-4.8, 4.5, circle_eq, fontsize=12, color="purple",
        bbox=dict(facecolor="white", alpha=0.6))

# Axes and meshgrid
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.6)

plt.savefig('2.png')
plt.show()

