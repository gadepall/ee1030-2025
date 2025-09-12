import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, 1, -1])
b = np.array([1, -1, 1])
origin = np.array([0, 0, 0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(*origin, *a, color='r', label='a = i + j - k')
ax.quiver(*origin, *b, color='b', label='b = i - j + k')

limit = 1.5
ax.set_xlim([-limit, limit])
ax.set_ylim([-limit, limit])
ax.set_zlim([-limit, limit])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('3D Vector Plot')

plt.savefig("3d_vector_plot.png")  # Save plot to file instead of plt.show()
