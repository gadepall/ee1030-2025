import matplotlib.pyplot as plt
import numpy as np

# Line equation: -2x + 3y = 6
# Solve for y: y = (2x + 6)/3

# Define x values for plotting
x = np.linspace(-10, 10, 400)
y = (2 * x + 6) / 3

# Find intercepts
# X-intercept: set y = 0 → -2x = 6 → x = -3 → A = (-3, 0)
# Y-intercept: set x = 0 → 3y = 6 → y = 2 → B = (0, 2)
A = (-3, 0)
B = (0, 2)

# Plot the line
plt.plot(x, y, label='Line: -2x + 3y = 6', color='blue')

# Mark the intercepts
plt.scatter(*A, color='red', zorder=5)
plt.scatter(*B, color='green', zorder=5)

# Annotate the points
plt.text(A[0]-1, A[1]-0.5, f'A {A}', color='red', fontsize=12)
plt.text(B[0]+0.2, B[1]+0.2, f'B {B}', color='green', fontsize=12)

# Axes lines
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Graph settings
plt.title('Graph of the Line -2x + 3y = 6')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Show the plot
plt.show()
