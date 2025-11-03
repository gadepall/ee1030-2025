import numpy as np
import matplotlib.pyplot as plt

xx, yy = np.meshgrid(np.linspace(-5, 5, 40), np.linspace(-5, 5, 40))

zz1 = np.zeros_like(xx)

zz2 = (3*xx - yy) / 4

zz3 = (2*xx + yy - 3) / 2

zz4 = (xx - 2*yy + 3) / 2

n1 = np.array([1,3,0], dtype=float)
n2 = np.array([3,-1,-4], dtype=float)

d_vec = np.cross(n1,n2)
d_vec = d_vec/np.linalg.norm(d_vec)

y0 = 0
x0 = 6 - 3*y0
z0 = (3*x0 - y0)/4
point_on_line = np.array([x0,y0,z0],dtype=float)

t_vals = np.linspace(-5,5,50)
line_points = point_on_line[:,None] + d_vec[:,None]*t_vals

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(xx, yy, zz1, alpha=0.3, color="green")
ax.text(2,2,0,"Given 1", color="black", fontsize=11)

ax.plot_surface(xx, yy, zz2, alpha=0.3, color="green")
ax.text(2,-2,(3*2-(-2))/4,"Given 2", color="black", fontsize=11)

ax.plot(line_points[0], line_points[1], line_points[2], color="purple", linewidth=2)
ax.text(*point_on_line,"Intersection", color="black", fontsize=11)

ax.plot_surface(xx, yy, zz3, alpha=0.4, color="red")
ax.text(2,2,(2*2+2-3)/2,"Req 1", color="black", fontsize=11)

ax.plot_surface(xx, yy, zz4, alpha=0.4, color="red")
ax.text(2,2,(2-4+3)/2,"Req 2", color="black", fontsize=11)

ax.scatter(0,0,0, color="black", s=60)
ax.text(0.2,0.2,0.2,"Origin", color="black", fontsize=11)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.tight_layout()
plt.savefig("../figs/img2.png", dpi=300)

