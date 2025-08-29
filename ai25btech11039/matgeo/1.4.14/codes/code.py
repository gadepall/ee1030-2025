import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([-6, 10, 0.0])
B = np.array([-4,  6, 0.0])
C = np.array([ 3, -8, 0.0])

t = np.linspace(-0.15, 1.15, 200)
line = A[:, None] + (C - A)[:, None] * t

AB = np.linalg.norm(A - B)
BC = np.linalg.norm(B - C)
AC = np.linalg.norm(A - C)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(line[0], line[1], line[2], linewidth=2, label="Line through A and C")
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], linestyle="--", linewidth=2, label="AB")
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], linestyle="--", linewidth=2, label="BC")

ax.scatter([A[0]], [A[1]], [A[2]], marker="o", s=60, label="A (-6, 10, 0)")
ax.scatter([B[0]], [B[1]], [B[2]], marker="s", s=60, label="B (-4, 6, 0)")
ax.scatter([C[0]], [C[1]], [C[2]], marker="^", s=70, label="C (3, -8, 0)")

def annot(pt, name, dx=0.6, dy=0.6, dz=0.2):
    ax.text(pt[0] + dx, pt[1] + dy, pt[2] + dz, name, fontsize=11)

annot(A, "A")
annot(B, "B")
annot(C, "C")

txt = (
    f"|AB| = {AB:.3f}\n"
    f"|BC| = {BC:.3f}\n"
    f"|AC| = {AC:.3f}\n"
    f"AB:BC ≈ {AB/BC:.3f} ≈ 2:7\n"
    f"AB/AC ≈ {AB/AC:.3f} ≈ 2/9"
)
ax.text2D(0.02, 0.98, txt, transform=ax.transAxes, fontsize=10, va="top", ha="left")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("3D view: Collinearity of A, B, C")

xs = np.array([A[0], B[0], C[0]])
ys = np.array([A[1], B[1], C[1]])
padx = (xs.max() - xs.min()) * 0.25 + 1
pady = (ys.max() - ys.min()) * 0.25 + 1
ax.set_xlim(xs.min() - padx, xs.max() + padx)
ax.set_ylim(ys.min() - pady, ys.max() + pady)
ax.set_zlim(-1.5, 1.5)

ax.legend(loc="upper right")
plt.tight_layout()
plt.show()
