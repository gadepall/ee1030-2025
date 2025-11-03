import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.suptitle("Q 5.3.34")

D = np.array([6, 18]).reshape(-1, 1)
M = np.array([[2, -5], [6, -15]])

A = np.concatenate((M, D), axis=1).reshape(2, 3)

if (r := np.linalg.matrix_rank(A)) == 1:
    print(f"Rank of augmented matrix is {r}, hence infinite solutions exist.")
    x = np.linspace(-5, 5, 10)
    y1 = (6 - 2*x)/5
    ax.plot(x, y1, label="2x - 5y = 6")
    y2 = (18 - 6*x)/15
    ax.plot(x, y2, label="6x - 15y = 18")

ax.grid()
ax.legend()
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.axis([-5, 5, -5, 5])
ax.set_xticks(np.arange(-5, 6, 2))
ax.set_yticks(np.arange(-5, 6, 2))

ax.set_aspect('equal')

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# plt.show()
fig.savefig("../figs/plot.png")