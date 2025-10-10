import numpy as np
import matplotlib.pyplot as plt

A = np.array([2, -1, 1])
B = np.array([1, -3, -5])
C = np.array([3, -4, -4])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

triangle = np.array([A, B, C, A])
ax.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], 'b-', marker='o')

for point, name in zip([A, B, C], ['A', 'B', 'C']):
    ax.text(point[0], point[1], point[2], f'{name} {point.tolist()}', color='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Triangle ABC')
plt.show()

