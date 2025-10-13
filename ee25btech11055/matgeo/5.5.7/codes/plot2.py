import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

A = np.array([[3, 0, -1], [2, 3, 0], [0, 4, 1]])

x = np.array([1, 1, 1])
b = A @ x
c = LA.inv(A) @ b
print(x,A,b,c,sep='\n')


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(121, projection="3d")

ax.quiver(0, 0, 0, x[0], x[1], x[2], color="red", label="Original Vector")
ax.text(x[0], x[1], x[2], " V1")
ax.quiver(0, 0, 0, b[0], b[1], b[2], color="blue", label="Modified Vector")
ax.text(b[0], b[1], b[2], " V2")

ax2 = fig.add_subplot(122, projection="3d")

ax2.quiver(0, 0, 0, b[0], b[1], b[2], color="blue", label="Modified Vector")
ax2.text(b[0], b[1], b[2], " V2")
ax2.quiver(0, 0, 0, c[0], c[1], c[2], color="green", label="Reverted Vector")
ax2.text(c[0], c[1], c[2], " V3")


ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("5.5.7")
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.legend()
ax.grid(True)

ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")
ax2.set_zlabel("Z-axis")
ax2.set_title("5.5.7")
ax2.set_xlim([-10, 10])
ax2.set_ylim([-10, 10])
ax2.set_zlim([-10, 10])
ax2.legend()
ax2.grid(True)

plt.savefig("../figs/python.png")
plt.show()
