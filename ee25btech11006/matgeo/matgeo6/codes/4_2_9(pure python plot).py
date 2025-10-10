import numpy as np
import matplotlib.pyplot as plt

# Define the line equation x + y = 4
# We parametrize it as y = 4 - x
x_vals = np.linspace(-2, 6, 400)
y_vals = 4 - x_vals

# Normal vector n = [1, 1]
n = np.array([1, 1])
# Direction vector d = [1, -1]
d = np.array([1, -1])

# Choose a point on the line, e.g., when x=2, y=2
point_on_line = np.array([2, 2])

# Plot the line
plt.plot(x_vals, y_vals, label='Line: $x + y = 4$', color='blue')

# Plot the normal vector starting at the point_on_line
plt.quiver(point_on_line[0], point_on_line[1], n[0], n[1],
           angles='xy', scale_units='xy', scale=1, color='red', label='Normal Vector')

# Plot the direction vector starting at the same point
plt.quiver(point_on_line[0], point_on_line[1], d[0], d[1],
           angles='xy', scale_units='xy', scale=1, color='orange', label='Direction Vector')

# Annotate the point and vectors
plt.scatter(point_on_line[0], point_on_line[1], color='black')
plt.annotate('Point on line (2, 2)',
             (point_on_line[0], point_on_line[1]), textcoords="offset points", xytext=(10,-10), ha='center')

plt.annotate('Normal [1, 1]',
             (point_on_line[0]+n[0], point_on_line[1]+n[1]), textcoords="offset points", xytext=(10,10), color='red')

plt.annotate('Direction [1, -1]',
             (point_on_line[0]+d[0], point_on_line[1]+d[1]), textcoords="offset points", xytext=(10,-20), color='orange')

# Axes settings
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

# Save the figure
plt.savefig('fig6.png')

# Show the plot
plt.show()