import numpy as np
import matplotlib.pyplot as plt

d1 = np.array([7, -5, 1])
d2 = np.array([1, 2, 3])
m = len(d1)

d = d1[0]*d2[0]+d1[1]*d2[1]+d1[2]*d2[2]
A = np.array([5, -2, 0])
B = np.array([0, 0, 0])

scale_factor = 10 # How long to make the line segments
line1_points = np.array([A - scale_factor * d1, A + scale_factor * d1])
line2_points = np.array([B - scale_factor * d2, B + scale_factor * d2])

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

ax.plot(line1_points[:, 0], line1_points[:, 1], line1_points[:, 2], 'b-', label='L1 (Point A, Dir d1)')
ax.plot(line2_points[:, 0], line2_points[:, 1], line2_points[:, 2], 'g-', label='L2 (Point B, Dir d2)')

ax.scatter(A[0], A[1], A[2], color='blue', s=100)
ax.text(A[0], A[1], A[2], f'  A{tuple(A)}', color='blue')
ax.scatter(B[0], B[1], B[2], color='green', s=100)
ax.text(B[0], B[1], B[2], f'  B{tuple(B)}', color='green')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('3D Lines L1 and L2')
ax.legend(['L1','L2'])
ax.view_init(36,-135)
plt.grid()
plt.tight_layout()

plt.savefig("../figs/plot_p.jpg")
plt.show()
