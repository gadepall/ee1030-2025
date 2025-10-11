import numpy as np
import matplotlib.pyplot as plt

# Local imports (assuming these scripts are available and in PYTHONPATH)
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Given intersection parameter lambda (from your C-types code or calculation)
lam = -35/19  # approx -1.8421

# Calculate intersection parameters s and t for the lines
# The two parametric lines from your problem:

# Line 1:
# x = 5 + (5*lam + 2)*t
# y = 2 - 5*t
# z = 1 + t

# Line 2:
# x = s
# y = -0.5 + 2*lam*s
# z = 1 + 3*s

# We want to find s, t such that both lines intersect

# From parametric equality:
# 5 + (5*lam + 2)*t = s      ...(1)
# 2 - 5*t = -0.5 + 2*lam*s   ...(2)
# 1 + t = 1 + 3*s            ...(3)

# Solve (3):
# t = 3*s

# Substitute into (1):
# 5 + (5*lam + 2)*3*s = s
# 5 + 3*(5*lam + 2)*s = s
# 5 = s - 3*(5*lam + 2)*s = s*(1 - 3*(5*lam + 2))
# s = 5 / (1 - 3*(5*lam + 2))

denom = 1 - 3*(5*lam + 2)
s = 5 / denom

# Then t = 3*s
t = 3*s

# Calculate intersection point from line 2 (or line 1)
inter_point = np.array([
    s,
    -0.5 + 2*lam*s,
    1 + 3*s
])

print(f"Intersection parameters: s = {s:.5f}, t = {t:.5f}")
print(f"Intersection Point: ({inter_point[0]:.5f}, {inter_point[1]:.5f}, {inter_point[2]:.5f})")

# Define parametric lines for plotting near intersection point

def line1(t_vals):
    x = 5 + (5*lam + 2)*t_vals
    y = 2 - 5*t_vals
    z = 1 + t_vals
    return x, y, z

def line2(s_vals):
    x = s_vals
    y = -0.5 + 2*lam*s_vals
    z = 1 + 3*s_vals
    return x, y, z

# Plot ranges close to intersection
t_vals = np.linspace(t - 1, t + 1, 100)
s_vals = np.linspace(s - 1, s + 1, 100)

x1, y1, z1 = line1(t_vals)
x2, y2, z2 = line2(s_vals)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x1, y1, z1, label='Line 1', color='blue', linewidth=2)
ax.plot(x2, y2, z2, label='Line 2', color='red', linewidth=2)

# Mark intersection
ax.scatter(*inter_point, color='green', s=80, label='Intersection Point')

# Annotate intersection point
ax.text(inter_point[0], inter_point[1], inter_point[2],
        f"A\n({inter_point[0]:.2f}, {inter_point[1]:.2f}, {inter_point[2]:.2f})",
        color='green', fontsize=12, ha='center', va='bottom')

# Axis labels and title
ax.set_xlabel("X axis", fontsize=12)
ax.set_ylabel("Y axis", fontsize=12)
ax.set_zlabel("Z axis", fontsize=12)
ax.set_title("3D Plot of Two Lines and their Intersection", fontsize=14)

ax.legend()
ax.grid(True)
ax.view_init(elev=20, azim=45)

plt.tight_layout()
plt.show()

