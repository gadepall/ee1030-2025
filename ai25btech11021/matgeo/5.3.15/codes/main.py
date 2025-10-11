import matplotlib.pyplot as plt
import numpy as np

# 1. Define the range for x
x = np.linspace(-10, 10, 400)

# 2. Define the equations in slope-intercept form (y = mx + b)
# Equation 1: y = (1/2)x + 3/2
y1 = (1/2) * x + 3/2

# Equation 2: y = (1/2)x - 5/4
y2 = (1/2) * x - 5/4

# 3. Create the plot
plt.figure(figsize=(8, 6))

# Plot the lines
plt.plot(x, y1, label='$x - 2y + 3 = 0$ ($y = 0.5x + 1.5$)', color='blue')
plt.plot(x, y2, label='$2x - 4y = 5$ ($y = 0.5x - 1.25$)', color='red', linestyle='--')

# 4. Customize the plot
plt.title('Graph of a Pair of Linear Equations (Parallel Lines)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='black', linewidth=0.5) # x-axis line
plt.axvline(0, color='black', linewidth=0.5) # y-axis line
plt.grid(color='gray', linestyle=':', linewidth=0.5)
plt.legend()
plt.axis('equal') # Ensures that the slopes look correct
plt.show()