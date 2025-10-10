import numpy as np
import matplotlib.pyplot as plt

# Define functions
def parabola(x):
    return (3/4) * x**2

def line(x):
    return (3/2) * x + 6

# Intersection points
x1, x2 = -2, 4

# Generate x values
x_vals = np.linspace(x1-1, x2+1, 400)

# Plot curves
plt.figure(figsize=(8,6))
plt.plot(x_vals, parabola(x_vals), label=r'$y=\frac{3}{4}x^2$', color='blue')
plt.plot(x_vals, line(x_vals), label=r'$y=\frac{3}{2}x+6$', color='red')

# Fill area between curves
x_fill = np.linspace(x1, x2, 400)
plt.fill_between(x_fill, line(x_fill), parabola(x_fill), where=line(x_fill)>=parabola(x_fill), 
                 color='lightgreen', alpha=0.6, label="Enclosed Area")

# Mark intersection points
plt.scatter([x1, x2], [parabola(x1), parabola(x2)], color='black', zorder=5)

# Labels and legend
plt.title("Area Enclosed by Parabola and Line")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)


plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/9.3.3/figs/fig.png')
plt.show()

