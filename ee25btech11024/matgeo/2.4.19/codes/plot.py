iiport numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([1,1,-1])
B = np.array([2,-1,3])
C = np.array([2,0,-3])
D = np.array([3,-2,1])

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111, projection = '3d')

ax.quiver(A[0], A[1], A[2], B[0]-A[0], B[1]-A[1], B[2]-A[2], color = 'g', label = 'AB')
ax.quiver(C[0], C[1], C[2], D[0]-C[0], D[1]-C[1], D[2]-C[2], color = 'r', label = 'CD', linewidth=3, arrow_length_ratio=0.4)
ax.quiver(C[0], C[1], C[2], D[0]-C[0], D[1]-C[1], D[2]-C[2], color='black',linestyle='--', label='Projection of AB on CD')

ax.scatter(*A, color='green', s=50)
ax.scatter(*B, color= 'blue', s=50)
ax.scatter(*C, color= 'red', s=50)
ax.scatter(*D, color= 'black', s=50)

ax.text(A[0]+0.1, A[1]-0.3, A[2]+0.3, "A(1,1,-1)")
ax.text(B[0]+0.3, B[1]+0.3, B[2]+0.3, "B(2,-1,3)")
ax.text(C[0]+0.1, C[1]-0.3, C[2]+0.3, "C(2,0,-3)")
ax.text(D[0]+0.3, D[1]+0.3, D[2]+0.3, "D(3,-2,1)")


ax.set_xlabel("X - AXIS")
ax.set_ylabel("Y - AXIS")
ax.set_zlabel("Z - AXIS")
ax.set_title("Projection Vector of AB along CD")

ax.legend()
ax.set_box_aspect([1, 1, 1])
ax.view_init(elev=10, azim=-120)
plt.savefig("fig.png", dpi=300)
plt.show()
