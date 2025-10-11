import numpy as np
import matplotlib.pyplot as plt
from call import give_data
Ax, Ay, Az, Bx, By, Bz = give_data()
lambda_val = -2.5
a = np.array([Ax, Ay, Az])   
b = np.array([Bx, By, Bz])   
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='Vector a')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label='Vector b')
ax.text(a[0], a[1], a[2], 'a', fontsize=12)
ax.text(b[0], b[1], b[2], 'b', fontsize=12)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Orthogonal Vectors a and b")
ax.legend()
plt.savefig("../figs/plot.png")
plt.show()

