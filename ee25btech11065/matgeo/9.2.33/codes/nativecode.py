import numpy as np
import matplotlib.pyplot as plt

def parabola(x):
    return x**2

def line(x):
    return x + 2

x_range = np.linspace(-3, 4, 400)
y_parabola = parabola(x_range)
y_line = line(x_range)

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x_range, y_parabola, 'b-', label='$y = x^2$')
ax.plot(x_range, y_line, 'r-', label='$y = x + 2$')

x_fill = np.linspace(-1, 2, 100)
ax.fill_between(x_fill, parabola(x_fill), line(x_fill), color='gray', alpha=0.3, label='Area = 9/2')

intersection_points_x = [-1, 2]
intersection_points_y = [1, 4]
ax.plot(intersection_points_x, intersection_points_y, 'ko')

ax.text(-1, 1, ' (-1, 1)', verticalalignment='bottom', horizontalalignment='right')
ax.text(2, 4, ' (2, 4)', verticalalignment='bottom', horizontalalignment='left')

ax.set_title('Area Bounded by Parabola and Line')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True, linestyle='--')
ax.legend()

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

ax.set_aspect('equal', adjustable='box')

plt.show()


