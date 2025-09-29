import matplotlib.pyplot as plt
import numpy as np

# Constants
sqrt3 = np.sqrt(3)
A = 2 + sqrt3
B = 1
C = 8 * np.sqrt(2 + sqrt3)

# Create x values
x = np.linspace(-10, 10, 400)

# Two lines: one for +C and one for -C
y1 = -A * x + C  # Line 1
y2 = -A * x - C  # Line 2

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r'$(2+\sqrt{3})x + y = +8\sqrt{2+\sqrt{3}}$', color='blue')
plt.plot(x, y2, label=r'$(2+\sqrt{3})x + y = -8\sqrt{2+\sqrt{3}}$', color='green')

# Plot origin and axes
plt.plot(0, 0, 'ro', label='Origin')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Formatting
plt.title('Graph of the Lines with Given Perpendicular Distance and Angle')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.axis('equal')
plt.legend()

# Save the plot
plt.savefig("graph7.png")
plt.show()

