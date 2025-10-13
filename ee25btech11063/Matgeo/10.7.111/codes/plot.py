import matplotlib.pyplot as plt
import numpy as np
import math

# Given values
a = 5                  # y-coordinate of center
r = math.sqrt(5)       # radius
center = (0, a)
A1 = (2, 4)
B1 = (-2, 6)

# Generate circle
theta = np.linspace(0, 2 * np.pi, 400)
x_circle = r * np.cos(theta)
y_circle = a + r * np.sin(theta)

# Tangent line y = 2x
x_line = np.linspace(-4, 4, 200)
y_line = 2 * x_line

# Plot circle and tangent
plt.plot(x_circle, y_circle, label='Circle', color='blue')
plt.plot(x_line, y_line, color='red', linestyle='--', label='Tangent: y = 2x')

# Plot key points
plt.scatter(*center, color='black', s=60)
plt.scatter(*A1, color='green', s=60)
plt.scatter(*B1, color='orange', s=60)

# Draw radius line
plt.plot([center[0], A1[0]], [center[1], A1[1]], color='purple', linestyle=':')

# Plain text annotations (no boxes on points)
plt.text(2.1, 4.1, "A₁(2,4)", color='green', fontsize=10)
plt.text(-2.8, 6.1, "B₁(-2,6)", color='orange', fontsize=10)
plt.text(0.2, 5.1, "Center (0,5)", color='black', fontsize=10)

# Box below tangent equation showing radius
plt.text(1.5, -2.5, "r = √5", fontsize=11, color='purple',
         bbox=dict(facecolor='lavender', edgecolor='purple', boxstyle='round,pad=0.4'))

# Make it neat
plt.axis('equal')
plt.grid(True, linestyle=':')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Circle Tangent to y = 2x with Points A₁ and B₁')
plt.legend(loc='upper left')
plt.savefig('circle.png', dpi=300)
plt.show()

