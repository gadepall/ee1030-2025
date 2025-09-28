# Circle through (0,0), (a,0), (0,b) using the matrix method
# Equation: ||x||^2 + 2u^T x + f = 0
# Centre = -u

import numpy as np
import matplotlib.pyplot as plt

# --- Input values ---
a = 6.0
b = 4.0

# --- Build the 3x3 system A [u1, u2, f]^T = b_vec ---
A = np.array([
    [0.0,   0.0, 1.0],
    [2.0*a, 0.0, 1.0],
    [0.0, 2.0*b, 1.0]
], dtype=float)

b_vec = np.array([0.0, -a*a, -b*b], dtype=float)

# --- Solve for (u1, u2, f) ---
u1, u2, f = np.linalg.solve(A, b_vec)

# --- Centre and radius ---
cx, cy = -u1, -u2
r = np.hypot(cx, cy)

print(f"u = ({u1}, {u2}), f = {f}")
print(f"Centre = ({cx}, {cy})")
print(f"Radius = {r}")

# --- Plot the circle and points ---
theta = np.linspace(0, 2*np.pi, 400)
X = cx + r*np.cos(theta)
Y = cy + r*np.sin(theta)

plt.figure()
plt.plot(X, Y, label="Circle")
plt.scatter([0, a, 0], [0, 0, b], color="red", label="Given points")
plt.scatter([cx], [cy], color="green", marker="x", s=100, label="Centre")
plt.gca().set_aspect("equal", adjustable="box")
plt.title(f"Matrix Method: Centre=({cx:.2f},{cy:.2f}), r={r:.2f}")
plt.xlabel("x"); plt.ylabel("y")
plt.grid(True)

# Place legend outside (right side)
plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1.0))
plt.tight_layout()
plt.savefig("newcentre.png")
plt.show()

