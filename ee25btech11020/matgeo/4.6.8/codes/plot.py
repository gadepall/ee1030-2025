import numpy as np
import matplotlib.pyplot as plt

a, b, c, d1, d2 = 5, 2, -3, 17, 23

xx, yy = np.meshgrid(np.linspace(0, 8, 30), np.linspace(0, 8, 30))

zz1 = (a*xx + b*yy - d1) / (-c)
zz2 = (a*xx + b*yy - d2) / (-c)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=15,azim=90)
ax.plot_surface(xx, yy, zz1, alpha=0.5, color='red', label="Plane 1")
ax.plot_surface(xx, yy, zz2, alpha=0.5, color='yellow', label="Plane 2")

points = np.array([[2,2,-1],[3,4,2],[7,0,6],[4,3,1]])
ax.scatter(points[:,0], points[:,1], points[:,2], color='black', s=50)
ax.text(1,1,(d1 - a*1 - b*1)/c,"Plane 1")
ax.text(1,2,(d2 - a*1 - b*2)/c,"Plane 2")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.savefig("../figs/img2.png")
plt.show()

