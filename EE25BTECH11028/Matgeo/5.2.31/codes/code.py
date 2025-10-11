import numpy as np
import matplotlib.pyplot as plt

# Define x values
x = np.linspace(-5, 5, 400)

# Line 1: 2x + 3y = 8  => y = (8 - 2x)/3
y1 = (8 - 2*x)/3

# Line 2: 4x + 6y = 7  => y = (7 - 4*x)/6
y2 = (7 - 4*x)/6

# Plot the lines
plt.figure(figsize=(8,6))
plt.plot(x, y1, label='2x + 3y = 8', color='blue')
plt.plot(x, y2, label='4x + 6y = 7', color='red', linestyle='--')

# Labels and grid
plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualization of the system of equations')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.savefig("fig10.png")
plt.show()