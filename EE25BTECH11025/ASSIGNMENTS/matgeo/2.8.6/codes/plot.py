import numpy as np
import matplotlib.pyplot as plt
from call import give_data

x1, y1, a, b, c, x_img, y_img = give_data()
a, b, c = 1, -3, 4

x_vals = np.linspace(-5, 5, 100)
y_vals = (-(a*x_vals + c))/b
plt.plot(x_vals, y_vals, 'k-', label='Mirror Line')

plt.scatter([x1, x_img], [y1, y_img], c=['r','b'])
plt.text(x1, y1, 'P(1,2)', fontsize=12)
plt.text(x_img, y_img, "P'", fontsize=12)
plt.plot([x1, x_img], [y1, y_img], 'g--', label='Perpendicular')

plt.axis('equal')
plt.grid(True)
plt.title("Reflection of Point (1,2) in Line x - 3y + 4 = 0")
plt.savefig("../figs/plot.png")
plt.show()

