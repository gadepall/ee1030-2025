import numpy as np
import matplotlib.pyplot as plt

# --- Line y = x - 2 ---
x = np.linspace(-2, 6, 100)
y = x - 2

# --- Direction and Normal Vectors (from equation x - y - 2 = 0) ---
direction = np.array([1, 1])   # along the line
normal = np.array([1, -1])     # perpendicular to the line

# --- Choose a point on the line (2,0) ---
P = np.array([2, 0])

# --- Plot line ---
fig, ax = plt.subplots()
ax.plot(x, y, color="purple", linewidth=2, label="y = x - 2")

# --- Scatter the point ---
ax.scatter(*P, color="green", s=60)

# --- Labels ---
ax.text(P[0] + 0.2, P[1] - 0.3, f"P{tuple(P)}", color="green")

# --- Plot vectors ---
ax.arrow(P[0], P[1], direction[0], direction[1],
         head_width=0.2, color="red", length_includes_head=True)
ax.text(P[0] + direction[0] + 0.2, P[1] + direction[1], "Direction", color="red")

ax.arrow(P[0], P[1], normal[0], normal[1],
         head_width=0.2, color="blue", length_includes_head=True)
ax.text(P[0] + normal[0] + 0.2, P[1] + normal[1], "Normal", color="blue")

# --- Axes and formatting ---
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_title("Line y = x - 2 with Direction & Normal Vectors")
ax.set_aspect("equal")
ax.grid(True)
ax.legend()

plt.show()
  