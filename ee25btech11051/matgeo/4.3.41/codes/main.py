import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-10, 10, 100)

m = np.array([3, 7, 2], dtype=np.float64)
x = 5 + t * m[0]
y = -4 + t * m[1]
z = 6 + t * m[2]


fig = plt.figure()
ax = plt.subplot(111, projection='3d')  


ax.plot(x, y, z, label='3D Line', color='blue')
ax.scatter(5, -4, 6, color='red', label='Point (5, -4, 6)')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('3D Line from Vector Equation')

plt.savefig('/home/shreyas/GVV_Assignments/matgeo/4.3.41/figs/fig1.png')
plt.show()

