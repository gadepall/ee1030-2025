from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from random import randint

fig, ax = plt.subplots()
fig.suptitle("Q 4.13.5")

p = np.array([3/4, 1/2]).reshape(2, 1)  # point of concurrency
o = np.array([0, 0]).reshape(2, 1)  # origin


for _ in range(5):
    a = randint(-10, 10)
    b = randint(-10, 10)
    while b == 0:
        b = randint(-10, 10)
    c = -(3*a + 2*b)/4

    p_a = [-5, ( -c - a*(-5) )/b]
    p_b = [5, ( -c - a*(5) )/b]

    ax.plot([p_a[0], p_b[0]], [p_a[1], p_b[1]], label=f"{a}x + {b}y + {c} = 0")

ax.plot(p[0], p[1], 'ro', label="P")  # point of concurrency
ax.annotate("P", (p[0], p[1]), textcoords="offset points", xytext=(0,10), ha='center')


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