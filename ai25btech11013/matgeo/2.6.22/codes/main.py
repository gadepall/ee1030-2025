import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
A=np.array([2,1,3])
B=np.array([3,5,-2])
C=np.cross(A,B)
normC=linalg.norm(C)
fig=plt.figure()
ax = fig.add_subplot(111, projection='3d') 
O= [0, 0, 0] 
ax.quiver(*O, *A, color='r', label='a', linewidth=2) 
ax.quiver(*O, *B, color='g', label='b', linewidth=2)
ax.quiver(*O, *C, color='b', label='a × b', linewidth=2)
ax.text(A[0], A[1], A[2], 'a', color='r', fontsize=12)
ax.text(B[0], B[1], B[2], 'b', color='g', fontsize=12)
ax.text(C[0], C[1], C[2], 'a × b', color='b', fontsize=12)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-20,5]) 
ax.set_ylim([0,15])
ax.set_zlim([-5,10])
ax.set_title('plotting a,b,a×b')
plt.savefig("/home/gauthamp/ee1030-2025/ai25btech11013/matgeo/2.6.22/figs/plot.png")
plt.show()



