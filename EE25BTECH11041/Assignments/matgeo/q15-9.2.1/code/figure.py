import numpy as np
import matplotlib.pyplot as plt
import math

y = np.linspace(-2,4,300)
x = y*y
xl = np.linspace(0,10,300)
yl = (xl-3)/2

x1 = np.linspace(0,3, 200)
y1 = np.sqrt(x1)
x2 = np.linspace(3,9, 200)
y2 = np.sqrt(x2)
yl2 = (x2-3)/2

plt.fill_between(x1, y1, 0, color='skyblue', alpha=0.4) 
plt.fill_between(x2,y2, yl2, color='skyblue', alpha=0.4)
plt.annotate('Intersection (9, 3)', xy=(9, 3), xytext=(7, 4),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.plot(x,y, label="parabola")
plt.plot(xl,yl, label="line")
plt.grid()
plt.legend()

plt.savefig("figure.png", dpi=300)

plt.show()
