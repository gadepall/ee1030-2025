import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

a, b, c = 20, 23, 26
d = 69

xx, yy = np.meshgrid(range(-10, 11), range(-10, 11))
zz = (d - a*xx - b*yy) / c

ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane: 20x + 23y + 26z = 69')

plt.show()

