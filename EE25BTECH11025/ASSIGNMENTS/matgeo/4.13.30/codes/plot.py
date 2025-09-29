import matplotlib.pyplot as plt
import numpy as np

x = [-3/2, -3/2]
y = [5, -5]

X = [1, -1, 2]
Y = [0, 0, 0]

plt.plot(x, y, '-r')
plt.plot(X, Y, 'ko')

plt.text(0.6, 0.1, "(1,0)", fontsize=10, color="black")
plt.text(-1.1, 0.1, "(-1,0)", fontsize=10, color="black")
plt.text(2.1, 0.1, "(2,0)", fontsize=10, color="black")
plt.text(-1.51, 3.20, r"$x=\frac{3}{2}$", fontsize=13, color="black")

plt.axvline(x=0, color='k', linewidth=1.5)
plt.axhline(y=0, color='k', linewidth=1.5)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.savefig("../figs/plot.png")
plt.show()

