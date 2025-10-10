import numpy as np
import matplotlib.pyplot as plt

# Equation: x^2 = -12y  =>  y = -x^2/12
x = np.linspace(-20, 20, 400)   # range for x
y = -x**2 / 12

# Plot
plt.figure(figsize=(6,6))
plt.plot(x, y, 'b', label=r'$x^2 = -12y$')

# Axes setup
plt.axhline(0, color='black', linewidth=0.8)  # x-axis
plt.axvline(0, color='black', linewidth=0.8)  # y-axis
plt.grid(True, linestyle='--', alpha=0.6)

plt.title("Graph of $x^2 = -12y$")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
