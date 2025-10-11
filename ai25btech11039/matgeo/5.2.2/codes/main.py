
import os
import numpy as np
import matplotlib.pyplot as plt

# Solve intersection A p = b  (p = [u, v]^T)
A = np.array([[5.0, -4.0],
              [7.0,  6.0]])
b = np.array([-8.0, 9.0])
u0, v0 = np.linalg.solve(A, b)

# Lines (express v as a function of u)
u = np.linspace(-3, 3, 400)
v1 = (5*u + 8)/4          # 5u - 4v + 8 = 0
v2 = (9 - 7*u)/6          # 7u + 6v - 9 = 0

plt.figure(figsize=(7, 5))
plt.plot(u, v1, label=r"$5u-4v+8=0$", linewidth=2)
plt.plot(u, v2, label=r"$7u+6v-9=0$", linewidth=2)

# Mark the intersection point
plt.scatter([u0], [v0], zorder=5)
plt.annotate(fr"$\left({u0:.3f},\,{v0:.3f}\right)$",
             (u0, v0), textcoords="offset points", xytext=(8, 8))

# Axes, limits, labels
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)
plt.xlim(-3, 3); plt.ylim(-2, 4)
plt.grid(True, alpha=0.3)
plt.xlabel("$u$"); plt.ylabel("$v$")
plt.legend()
plt.title("Intersection of $5u-4v+8=0$ and $7u+6v-9=0$")

# Save
os.makedirs("figs", exist_ok=True)
plt.tight_layout()
plt.savefig("figs/5.2.2.png", dpi=300, bbox_inches="tight")
plt.show()
