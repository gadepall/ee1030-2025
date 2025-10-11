import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.suptitle("Q 5.2.3")

D = np.array([-12, -24]).reshape(-1, 1)
M = np.array([[9, 3], [18, 6]])

A = np.concatenate((M, D), axis=1).reshape(2, 3)

if (r := np.linalg.matrix_rank(A)) == 1:
    print(f"Rank of augmented matrix is {r}, hence infinite solutions exist.")
    x = np.linspace(-5, 5, 100)
    y = (-4 - 3*x)/1
    ax.plot(x, y, label="3x + y = -4")
else:
    X = np.linalg.inv(M) @ D
    print(f"Solution: x = {X[0,0]}, y = {X[1,0]}")

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