import numpy as np
import matplotlib.pyplot as plt

# Given vertices
A = np.array([3.0, 0.0])
B = np.array([6.0, 0.0])

# Midpoint and side/height
M = (A + B) / 2
AB = B - A
side = np.linalg.norm(AB)
h = (np.sqrt(3) / 2) * side

# Unit vector perpendicular to AB
perp = np.array([-AB[1], AB[0]]) / np.linalg.norm(AB)

# Two possible third vertices
C1 = M + h * perp   # above x-axis
C2 = M - h * perp   # below x-axis

fig, ax = plt.subplots(figsize=(6, 6))

# Plot triangles (above and below)
ax.plot([A[0], B[0], C1[0], A[0]], [A[1], B[1], C1[1], A[1]], label="Triangle (above)")
ax.plot([A[0], B[0], C2[0], A[0]], [A[1], B[1], C2[1], A[1]], label="Triangle (below)")

# Mark points
for p in (A, B, C1, C2):
    ax.scatter(p[0], p[1])

# Label points (use annotate to offset labels)
ax.annotate("A(3,0)", xy=A, xytext=(-10, 8), textcoords="offset points", ha="right", va="bottom")
ax.annotate("B(6,0)", xy=B, xytext=(10, 8), textcoords="offset points", ha="left", va="bottom")
ax.annotate(f"C1({C1[0]:.2f},{C1[1]:.2f})", xy=C1, xytext=(0, 8), textcoords="offset points", ha="center", va="bottom")
ax.annotate(f"C2({C2[0]:.2f},{C2[1]:.2f})", xy=C2, xytext=(0, -10), textcoords="offset points", ha="center", va="top")

# Axes/formatting
ax.axhline(0, linewidth=0.5)
ax.axvline(0, linewidth=0.5)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)
ax.legend()
ax.set_title("Equilateral triangles for A(3,0), B(6,0)")

# Save and show
plt.savefig("triangle.png", dpi=200, bbox_inches="tight")
plt.show()


