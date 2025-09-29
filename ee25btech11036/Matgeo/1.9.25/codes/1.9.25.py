import numpy as np
import matplotlib.pyplot as plt

# Parameters
a, b = 2, 3   # You can change values here

# Points
A = np.array([a+b, b-a])
B = np.array([a-b, a+b])
P = np.array([4, 6])   # sample point

# Locus line: bx = ay -> y = (b/a) x (if a != 0)
x_vals = np.linspace(-10, 10, 400)
if a != 0:
    y_vals = (b/a) * x_vals
else:
    x_vals = np.full_like(x_vals, 0)
    y_vals = np.linspace(-10, 10, 400)

# Plot locus line
plt.plot(x_vals, y_vals, 'r-', label=r'$bx = ay$ (matrix form)')

# Plot points A, B, and P
plt.scatter(*A, color='green', s=70, label='Point A')
plt.scatter(*B, color='purple', s=70, label='Point B')
plt.scatter(*P, color='blue', s=70, label='Sample P')

# Draw distances PA and PB
plt.plot([P[0], A[0]], [P[1], A[1]], 'g--', alpha=0.7)
plt.plot([P[0], B[0]], [P[1], B[1]], 'm--', alpha=0.7)

# Distance check
dist_PA = np.linalg.norm(P - A)
dist_PB = np.linalg.norm(P - B)

plt.title(f"Locus from Matrix Condition\n|PA| = {dist_PA:.2f}, |PB| = {dist_PB:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axis("equal")
plt.show()
