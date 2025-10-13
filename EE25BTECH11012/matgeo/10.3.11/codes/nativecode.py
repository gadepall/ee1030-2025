import numpy as np
import matplotlib.pyplot as plt

# Create the figure and axis
fig, ax2 = plt.subplots()
fig.suptitle('Graphs of Normal to the Curve', fontsize=16)

# Curve: 2y + x^2 = 3  =>  y = (3 - x^2)/2
# Point: (1, 1)
# Normal Line: y = x
# Tangent Line at (1,1): y = -x + 2

# Generate x-values for the curve
x_curve2 = np.linspace(-3, 4, 400)
y_curve2 = (3 - x_curve2**2) / 2

# Generate x-values for the lines
x_line2 = np.linspace(-2, 4, 100)
y_normal = x_line2
y_tangent2 = -x_line2 + 2

# Plot the curve, normal, tangent, and the point
ax2.plot(x_curve2, y_curve2, label='Curve: $2y+x^2=3$', color='blue')
ax2.plot(x_line2, y_normal, label='Normal: $y=x$', color='green')
ax2.plot(x_line2, y_tangent2, label='Tangent: $y=-x+2$', color='red', linestyle='--')
ax2.scatter([1], [1], color='purple', s=100, zorder=5, label='Point (1, 1)')

# Formatting for the plot
ax2.set_title('10.3.11: Normal to $2y+x^2=3$', fontsize=12)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()
ax2.set_aspect('equal', adjustable='box')
ax2.set_xlim([-2, 4])
ax2.set_ylim([-2, 4])

# Display the figure
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()