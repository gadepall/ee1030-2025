import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")
fig.suptitle("Q 4.8.36")
K = 10


A = np.array([3, -1, 2]).reshape(-1, 1)
B = np.array([5, 2, 4]).reshape(-1, 1)
C = np.array([-1, -1, 6]).reshape(-1, 1)
P = np.array([6, 5, 9]).reshape(-1, 1)

n = np.cross((A - B).T, (A - C).T).T
n = n/np.gcd.reduce(n)
print(f"Normal vector: {n}")

c = n.T @ A
print(f"Constant c: {c[0,0]}")

d = abs(n.T @ P - c)/np.linalg.norm(n)
print(f"Distance of point from plane: {d[0,0]}")

xx, yy = np.meshgrid(np.linspace(-K, K+1, 200), np.linspace(-K, K+1, 200))
z = -(n[0,0] * xx + n[1,0] * yy - c[0,0])/n[2,0]
# z = np.arange(-K, K+1)

ax.plot_surface(xx, yy, z, alpha=1, label="Plane")


ax.plot(*A.flatten(), marker="o", color="red", label="A")
ax.plot(*B.flatten(), marker="o", color="blue", label="B")
ax.plot(*C.flatten(), marker="o", color="green", label="C")
ax.plot(*P.flatten(), marker="o", color="orange", label="P")

ax.grid()
ax.legend()
ax.plot((-K, K), (0, 0), (0, 0), color="black", label="X-axis")
ax.plot((0, 0), (-K, K), (0, 0), color="black", label="Y-axis")
ax.plot((0, 0), (0, 0), (-K, K), color="black", label="Z-axis")
ax.axis([-K, K, -K, K, -K, K])
ax.set_xticks(np.arange(-K, K+1, 2))
ax.set_yticks(np.arange(-K, K+1, 2))
ax.set_zticks(np.arange(-K, K+1, 2))

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.view_init(30, -160)

# plt.show()
fig.savefig("../figs/plot.png")