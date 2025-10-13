import numpy as np
import matplotlib.pyplot as plt

# Given data
O = (2, 1)
r = 4
P = (4, 5)
T1 = (2, 5)
T2 = (5.2, 3.4)
area = 8  # precomputed

# Circle coordinates
theta = np.linspace(0, 2*np.pi, 400)
x_circle = O[0] + r * np.cos(theta)
y_circle = O[1] + r * np.sin(theta)

# Tangent line equations
def tangent1(x): return np.full_like(x, 5.0)                     # y = 5
def tangent2(x): return -4/3 * x + 31/3                          # y = -4/3x + 31/3

# Range for plotting
x_vals = np.linspace(-3, 9, 400)

# Plot everything
plt.figure(figsize=(7,7))
plt.plot(x_circle, y_circle, 'b-', label='Circle: (x-2)² + (y-1)² = 16')
plt.plot(x_vals, tangent1(x_vals), 'g--', label='Tangent 1: y = 5')
plt.plot(x_vals, tangent2(x_vals), 'm--', label='Tangent 2: y = -4/3x + 31/3')

# Points
plt.scatter(*O, color='k', s=60, label='Center O(2,1)')
plt.scatter(*P, color='r', s=60, label='External Point P(4,5)')
plt.scatter(*T1, color='g', s=70, marker='o', label='T₁(2,5)')
plt.scatter(*T2, color='m', s=70, marker='o', label='T₂(5.2,3.4)')

# Aesthetic tweaks
plt.title(f"Tangents from P(4,5) to Circle — Area = {area}")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis('equal')
plt.xlim(-3, 10)
plt.ylim(-4, 9)
plt.grid(True)
plt.legend(loc='upper right')
plt.savefig("../figs/img2.png")
