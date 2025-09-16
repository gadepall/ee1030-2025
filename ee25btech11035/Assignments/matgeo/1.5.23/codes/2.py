import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = (-2, 3, 5)
B = (1, 2, 3)
C = (7, 0, -1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(*A, color="red", s=100, label=f"A{A}")
ax.scatter(*B, color="green", s=100, label=f"B{B}")
ax.scatter(*C, color="blue", s=100, label=f"C{C}")

ax.plot([A[0], B[0], C[0]],
        [A[1], B[1], C[1]],
        [A[2], B[2], C[2]],
        color="black", linewidth=2)

ax.set_title("Visualization of points A, B and C", fontsize=14)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()

plt.savefig('2.png')
plt.show()
