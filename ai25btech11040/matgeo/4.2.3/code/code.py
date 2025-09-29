import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.suptitle("Q 4.2.3")


# n represents the normal vector to the line -2x + 3y = 6
n = np.array([-2, 3]).reshape(-1, 1)
c = np.array([6])
o = np.array([0, 0]).reshape(-1, 1)

n_unit = n / np.linalg.norm(n)
d_unit = np.array([[0, -1], [1, 0]]).transpose() @ n_unit

print("Normal vector: \n", n_unit)
print("Direction vector: \n", d_unit)

x_eg = np.array([0, 1])
y_eg = (c[0] - n[0] * x_eg) / n[1]

ax.axline(*zip(x_eg, y_eg), color='blue', label='Given line')
ax.quiver(*o, *n_unit, color='r', label='Normal vector')
ax.quiver(*o, *d_unit, color='g', label='Direction vector')

ax.grid()
ax.legend()
ax.axis([-5, 5, -5, 5])
ax.set_xticks(np.arange(-5, 6, 1))
ax.set_yticks(np.arange(-5, 6, 1))
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# plt.show()
fig.savefig("../figs/plot.png")