import numpy as np
import matplotlib.pyplot as plt

# Load fraction solution
with open("fraction.txt", "r") as f:
    x_sol, y_sol = map(float, f.read().split())

# Define the two lines from the equations:
# Equation 1: x - y = -2 → y = x + 2
# Equation 2: 2x - y = 1 → y = 2x - 1

x_vals = np.linspace(0, 5, 100)
y1 = x_vals + 2
y2 = 2*x_vals - 1

# Plot the lines
plt.plot(x_vals, y1, label="x - y = -2")
plt.plot(x_vals, y2, label="2x - y = 1")

# Plot the intersection point
plt.scatter(x_sol, y_sol, color='red', s=100, label=f'Intersection ({x_sol},{y_sol})')

plt.xlabel("x (Numerator)")
plt.ylabel("y (Denominator)")
plt.title("Intersection of Two Lines (Fraction Solution)")
plt.grid(True)
plt.legend()
plt.show()

