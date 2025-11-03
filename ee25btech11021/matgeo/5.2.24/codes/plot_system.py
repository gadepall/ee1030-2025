import numpy as np
import matplotlib.pyplot as plt

p, q = 2, 3
x_sol, y_sol = 1, -1  # always same solution

x_vals = np.linspace(-5, 5, 400)

# Line 1: px + qy = p - q → y = (p - q - p*x)/q
y1 = (p - q - p*x_vals) / q

# Line 2: qx - py = p + q → y = (q*x - (p+q))/p
y2 = (q*x_vals - (p + q)) / p

plt.figure(figsize=(6,6))
plt.plot(x_vals, y1, label=f"{p}x + {q}y = {p-q}")
plt.plot(x_vals, y2, label=f"{q}x - {p}y = {p+q}")

# Intersection point
plt.plot(x_sol, y_sol, 'ro', label="Intersection (1, -1)")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.title("Intersection of Two Lines")
plt.show()

