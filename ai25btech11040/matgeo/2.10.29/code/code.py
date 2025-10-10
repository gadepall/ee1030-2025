import numpy as np

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")


a = np.array([2, -2, 0])
b = np.array([1, 1, -1])
c = np.array([3, 0, -1])

volume = a.T @ (np.cross(b, c))

print(f"Volume of the parallelopiped is {volume}")


O = np.array([0, 0, 0])
d = a + b
e = a + c
f = b + c
g = a + b + c

ax.plot3D(*zip(O, a), color="b")
ax.plot3D(*zip(O, b), color="b")
ax.plot3D(*zip(O, c), color="b")
ax.plot3D(*zip(a, d), color="b")
ax.plot3D(*zip(a, e), color="b")
ax.plot3D(*zip(b, d), color="b")
ax.plot3D(*zip(b, f), color="b")
ax.plot3D(*zip(c, e), color="b")
ax.plot3D(*zip(c, f), color="b")
ax.plot3D(*zip(d, g), color="b")
ax.plot3D(*zip(e, g), color="b")
ax.plot3D(*zip(f, g), color="b")

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

ax.view_init(elev=20, azim=225)

fig.savefig("../figs/plot.png")
