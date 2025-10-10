import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


a, b, c, d = 1, -1, 1, 5   


xx, yy = np.meshgrid(np.linspace(-10, 10, 50), np.linspace(-10, 10, 50))


zz = (d - a*xx - b*yy) / c


p0 = np.array([2, -1, 2])   
v = np.array([3, 4, 2])    

t = np.linspace(-5, 5, 50)
x_line = p0[0] + v[0]*t
y_line = p0[1] + v[1]*t
z_line = p0[2] + v[2]*t


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')


ax.plot(x_line, y_line, z_line, color='red', linewidth=2)

ax.text(-12, -22, -8, r'$\frac{x-2}{3}=\frac{y+1}{4}=\frac{z-2}{2}$', fontsize=12, color="black")
ax.text(-14,21,12, "x-y+z=5", fontsize=12, color="black")
ax.text(2.1, -0.9, 2.1, "(2,-1,2)", fontsize=12, color="black")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("../figs/plot.png")
plt.show()
