import sys
sys.path.insert(0, '/home/ganachari-vishwmabhar/Downloads/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt

# Local imports (as per second screenshot)
from line.funcs import *
from triangle.funcs import *

# Given line: x - 3y + 4 = 0  => a=1, b=-3, c=4
a, b, c = 1, -3, 4

# Given point
P = np.array([1, 2])

# Formula for image
x1, y1 = P
den = a**2 + b**2
x_img = ((b**2 - a**2)*x1 - 2*a*b*y1 - 2*a*c)/den
y_img = ((a**2 - b**2)*y1 - 2*a*b*x1 - 2*b*c)/den
P_img = np.array([x_img, y_img])

# Plot line
x_vals = np.linspace(-5, 5, 100)
y_vals = (-(a*x_vals + c))/b
plt.plot(x_vals, y_vals, 'k-', label='Mirror Line')

# Plot original point and image
plt.scatter([P[0], P_img[0]], [P[1], P_img[1]], c=['r','b'])
plt.text(P[0], P[1], 'P(1,2)', fontsize=12)
plt.text(P_img[0], P_img[1], "P'", fontsize=12)

# Connect them with perpendicular
plt.plot([P[0], P_img[0]], [P[1], P_img[1]], 'g--', label='Perpendicular')

# Settings
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title("Reflection of Point (1,2) in Line x - 3y + 4 = 0")
plt.savefig("../figs/plot.png")
plt.show()

