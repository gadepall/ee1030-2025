import numpy as np
import matplotlib.pyplot as plt

# Define the functions for the boundary curves
def parabola(x):
    return x**2

def line(x):
    return x + 2

# Create a range of x values to plot the full curves
x_full = np.linspace(-1, 3, 400)

# Calculate y values for the parabola and the line
y_parabola = parabola(x_full)
y_line = line(x_full)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the boundary curves
ax.plot(x_full, y_parabola, label=r'$y = x^2$', color='blue')
ax.plot(x_full, y_line, label=r'$y = x + 2$', color='red')
ax.axvline(x=-1, color='gray', linestyle='--')
ax.axvline(x=3, color='gray', linestyle='--')
ax.axhline(y=0, color='black', linewidth=0.5)

# Fill the area of the region correctly by splitting at the intersection point x=2.
# The area is bounded by y=0 below, and the minimum of y=x^2 and y=x+2 above.

# Area 1: from x=-1 to x=2, the parabola y=x^2 is the upper curve.
x1 = np.linspace(-1, 2, 200)
ax.fill_between(x1, 0, parabola(x1), color='skyblue', alpha=0.5, label='Region Area')

# Area 2: from x=2 to x=3, the line y=x+2 is the upper curve.
x2 = np.linspace(2, 3, 100)
ax.fill_between(x2, 0, line(x2), color='skyblue', alpha=0.5)

# Plot the intersection points and label them
ax.plot([-1, 2], [parabola(-1), parabola(2)], 'ro')
ax.annotate('(-1, 1)', (-1, 1), textcoords="offset points", xytext=(-15, 10), ha='center')
ax.annotate('(2, 4)', (2, 4), textcoords="offset points", xytext=(15, 10), ha='center')

# Set plot limits and labels
ax.set_ylim(-1, 12)
ax.set_title('Correct Area of the Defined Region')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True, linestyle='--')

plt.show()