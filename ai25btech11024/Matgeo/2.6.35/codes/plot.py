import numpy as np
import matplotlib.pyplot as plt

A=np.array([1,0,0])
B=np.array([0,1,0])
C=np.array([0,0,1])

fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw_vec(v, color, label):
    ax.quiver(0, 0, 0, v[0], v[1], v[2],
              color=color, arrow_length_ratio=0.1, label=label)

draw_vec(A,'r','A')
draw_vec(B,'b','B')
draw_vec(C,'g','C')

lim=3
ax.set_xlim([-lim,lim])
ax.set_ylim([-lim,lim])
ax.set_zlim([-lim,lim])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.savefig("../figs/img.png")
plt.show()
