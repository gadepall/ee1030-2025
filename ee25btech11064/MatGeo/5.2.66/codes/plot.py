import numpy as np
import matplotlib.pyplot as plt

# Define the x range
x_vals = np.linspace(-10, 70, 400)

# Equation 1: 2x + 3y = 11  --> y = (11 - 2x) / 3
y1_vals = (11 - 2 * x_vals) / 3

# Equation 2: 2x + 4y = -24  --> y = (-24 - 2x) / 4
y2_vals = (-24 - 2 * x_vals) / 4

# Line y = mx + 3 where m = -19/29
m = -19 / 29
y3_vals = m * x_vals + 3

# Plotting
plt.figure(figsize=(8, 6))

# Plot the lines
plt.plot(x_vals, y1_vals, label=r'$2x + 3y = 11$', color='blue')
plt.plot(x_vals, y2_vals, label=r'$2x + 4y = -24$', color='green')
plt.plot(x_vals, y3_vals, label=r'$y = \frac{-19}{29}x + 3$', color='red', linestyle='dashed')

# Mark the point (58, -35)
plt.scatter(58, -35, color='black', zorder=5)
plt.text(58, -35, f'  (58, -35)', fontsize=12, verticalalignment='bottom')

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of the Equations')

# Show legend
plt.legend()

# Set axis limits for better viewing
plt.xlim(-10, 70)
plt.ylim(-50, 20)

# Show grid
plt.grid(True)

# Show plot
plt.show()

