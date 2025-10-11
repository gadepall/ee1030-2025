import numpy as np
import matplotlib.pyplot as plt

h = np.array([1, 2, 3])
m = np.array([3, 2, -2])
kappa = np.linspace(-2, 2, 100)

x = h[0] + kappa*m[0]
y = h[1] + kappa*m[1]
z = h[2] + kappa*m[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='blue')
ax.scatter(h[0], h[1], h[2], color='red', s=50)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line through (1,2,3) parallel to [3,2,-2]')
ax.text(h[0], h[1], h[2], '(1,2,3)', color='red')

plt.show()
