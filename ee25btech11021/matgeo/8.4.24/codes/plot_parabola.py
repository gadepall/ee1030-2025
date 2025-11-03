import numpy as np
import matplotlib.pyplot as plt

# Use one k value from solution
k = 4  # choose k1

# Generate x values
x = np.linspace(-5, 10, 1000)

# Compute y^2
y_square = k*x - 8

# Only take real points
mask = y_square >= 0
x_real = x[mask]
y_real = np.sqrt(y_square[mask])

# Plot positive branch
plt.plot(x_real, y_real, 'b', label=f"Parabola y^2 - {k}x + 8 = 0")

# Plot negative branch
plt.plot(x_real, -y_real, 'b')

# Plot directrix
plt.axvline(x=1, color='r', linestyle='--', label='Directrix x=1')

# Plot focus
F_x = 1 + k/2
F_y = 0
plt.plot(F_x, F_y, 'go', label='Focus')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Parabola with Directrix and Focus")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

