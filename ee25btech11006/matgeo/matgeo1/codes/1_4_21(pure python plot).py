import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = (1, -2, 3)
B = (3, 4, -5)

P = ((2*B[0] + 3*A[0]) / 5,
     (2*B[1] + 3*A[1]) / 5,
     (2*B[2] + 3*A[2]) / 5)

Q = ((2*B[0] - 3*A[0]) / (2-3),
     (2*B[1] - 3*A[1]) / (2-3),
     (2*B[2] - 3*A[2]) / (2-3))

print("Internal Division Point:", P)
print("External Division Point:", Q)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')


ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='blue')


def plot_point(pt, label, color):
    ax.scatter(*pt, color=color, s=60)
    ax.text(pt[0], pt[1], pt[2], f"{label}{pt}", fontsize=10)

plot_point(A, "A", "red")
plot_point(B, "B", "red")
plot_point(P, "P", "green")   
plot_point(Q, "Q", "purple") 


ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Division of Line Segment')


ax.set_xlim(-4, 4)
ax.set_ylim(-15, 5)
ax.set_zlim(-5, 19)

plt.show()