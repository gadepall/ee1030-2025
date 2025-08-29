import numpy as np
import matplotlib.pyplot as plt

A = np.array([4.0, 4.0])
B = np.array([-2.0, 6.0])


n = 20
X = np.linspace(A[0], B[0], n+1)
Y = np.linspace(A[1], B[1], n+1)


midpoint = (A + B) / 2

plt.figure(figsize=(6,6))

plt.plot(X, Y, 'b-', label="Line segment")

plt.scatter(A[0], A[1], color='red', s=80, zorder=3, label="Point A (4,4)")
plt.scatter(B[0], B[1], color='green', s=80, zorder=3, label="Point B (-2,6)")

plt.scatter(midpoint[0], midpoint[1], color='purple', s=100, marker='x', zorder=4, label="Midpoint (1,5)")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line segment between A(4,4) and B(-2,6) with Midpoint")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.savefig("../figs/line_segment2.png")
plt.show()
