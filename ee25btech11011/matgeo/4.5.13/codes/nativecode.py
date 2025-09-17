import matplotlib.pyplot as plt
import numpy as np

# Point A
Ax, Ay = 2.0, 3.0

# --- Case 1: Line parallel to x-axis ---
n1 = (0, 1)
rhs1 = Ay   # (0,1)·x = y = 3

# --- Case 2: Line parallel to y-axis ---
n2 = (1, 0)
rhs2 = Ax   # (1,0)·x = x = 2

# --- Case 3: General line (example n = (2,-1)) ---
n3 = (2, -1)
rhs3 = n3[0]*Ax + n3[1]*Ay   # (2,-1)·(2,3) = 1

# --- Print results in vector notation ---
print(f"(0,1)·\\vec{{x}} = {rhs1}   (Line parallel to x-axis)")
print(f"(1,0)·\\vec{{x}} = {rhs2}   (Line parallel to y-axis)")
print(f"({n3[0]},{n3[1]})·\\vec{{x}} = {rhs3}   (General line through A)")

# --- Plotting ---
fig, ax = plt.subplots(figsize=(7,7))
x_vals = np.linspace(-5, 10, 400)
y_vals_range = np.linspace(-5, 10, 400)

# Case 1: horizontal line
ax.plot(x_vals, rhs1 * np.ones_like(x_vals), 'r--',
        label=rf"$(0,1)\cdot \vec{{x}} = {rhs1}$ (parallel to x-axis)")

# Case 2: vertical line
ax.plot(rhs2 * np.ones_like(y_vals_range), y_vals_range, 'b--',
        label=rf"$(1,0)\cdot \vec{{x}} = {rhs2}$ (parallel to y-axis)")

# Case 3: general line
y_vals = (rhs3 - n3[0]*x_vals) / n3[1]
ax.plot(x_vals, y_vals, 'g-',
        label=rf"$({n3[0]},{n3[1]})\cdot \vec{{x}} = {rhs3}$ (general line)")

# Mark point A
ax.scatter(Ax, Ay, color='black', zorder=5)
ax.text(Ax+0.2, Ay+0.2, r"$\vec{A}(2,3)$")

ax.set_xlim(-5, 10)
ax.set_ylim(-5, 10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
plt.savefig("fig6.png")
plt.show()