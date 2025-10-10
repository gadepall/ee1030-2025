# plot_specific_case.py
import numpy as np
import matplotlib.pyplot as plt

# Given values
x1, y1 = 2, -3
x2 = 10
d = 10

# Solve for y values
dx = x1 - x2
inside = d**2 - dx**2
if inside < 0:
    y_solutions = []
else:
    r = np.sqrt(inside)
    y_solutions = [y1 + r, y1 - r]

print("Solutions for y:", y_solutions)

# Circle centered at P with radius d
theta = np.linspace(0, 2*np.pi, 400)
circ_x = x1 + d * np.cos(theta)
circ_y = y1 + d * np.sin(theta)

# Plot
plt.figure(figsize=(6,6))
plt.plot(circ_x, circ_y, label=f'Circle: center P({x1},{y1}), r={d}')
plt.axvline(x=x2, linestyle=':', color='gray', label=f'x = {x2}')

# Point P
plt.scatter([x1], [y1], color='red', zorder=5)
plt.annotate(f'P({x1},{y1})', (x1,y1), textcoords="offset points", xytext=(6,6))

# Solutions Q
for i, yq in enumerate(y_solutions):
    plt.scatter([x2], [yq], color='blue', zorder=6)
    plt.annotate(f'Q{i+1}({x2},{yq:.1f})', (x2,yq), textcoords="offset points", xytext=(6,6))
    plt.plot([x1, x2], [y1, yq], linestyle='--', color='green')

plt.gca().set_aspect('equal', 'box')
plt.grid(True)
plt.legend()
plt.title('Specific Case: P(2,-3), Q(10,y), Distance=10')
plt.show()

