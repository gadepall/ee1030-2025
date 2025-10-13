import numpy as np
import matplotlib.pyplot as plt

h = np.array([5, -2, 4])
m = np.array([2, 1, 3])
lambd = np.linspace(-2, 2, 100)

x = h[0] + lambd * m[0]
y = h[1] + lambd * m[1]
z = h[2] + lambd * m[2]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, color='blue')
ax.scatter(h[0], h[1], h[2], color='red', s=50)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line through (5,-2,4) parallel to [2,1,3]')
ax.text(h[0], h[1], h[2], '(5,-2,4)', color='red')
plt.show()

