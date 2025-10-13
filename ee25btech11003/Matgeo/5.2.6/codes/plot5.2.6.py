import numpy as np
import matplotlib.pyplot as plt

# Create a range of x values
x = np.linspace(-10, 10, 400)

# Rearrange the equations into slope-intercept form (y = mx + c)
# Equation 1: 2x - 3y = 8  =>  y = (2/3)x - 8/3
y1 = (2/3)*x - (8/3)

# Equation 2: 4x - 6y = 9  =>  y = (4/6)x - 9/6  =>  y = (2/3)x - 3/2
y2 = (2/3)*x - (3/2)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the lines
plt.plot(x, y1, label='2x - 3y = 8', color='blue')
plt.plot(x, y2, label='4x - 6y = 9', color='red')

# Add titles and labels for clarity
plt.title('Plot of Inconsistent System of Equations', fontsize=16)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)

# Add a grid and set axis limits
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Display a legend to identify the lines
plt.legend()

# Show the plot
plt.show()
