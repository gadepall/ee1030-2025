
import numpy as np
import matplotlib.pyplot as plt

# Define equations of the lines
# Line 1: 3x - 5y - 4 = 0 -> y = (3x - 4)/5
# Line 2: 9x = 2y + 7 -> y = (9x - 7)/2

x = np.linspace(-5, 5, 400)
y1 = (3*x - 4)/5
y2 = (9*x - 7)/2

# Solve intersection using numpy
A = np.array([[3, -5], [9, -2]])
B = np.array([4, 7])
intersection = np.linalg.solve(A, B)

# Plotting


plt.figure(figsize=(7, 7))
plt.plot(x, y1, label='3x - 5y - 4 = 0', color='blue')
plt.plot(x, y2, label='9x - 2y - 7 = 0', color='red')

# Mark intersection point
plt.scatter(*intersection, color='black', zorder=5)
plt.text(intersection[0]+0.5, intersection[1]-0.5, 
         f'({intersection[0]:.2f}, {intersection[1]:.2f})', 
         fontsize=10, color="black")

# Labels and grid
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.title("Graph of the given equations")
# Save the plot to a file
plt.savefig('../figs/fig.png')

# Display the plot
plt.show()


