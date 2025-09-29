import numpy as np
import matplotlib.pyplot as plt

O = np.array([0, 0, 0])

a = np.array([0, 1, 0])
b = np.array([-1, 1, 0])
p = np.array([0, 0, 1])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot([O[0], a[0]], [O[1], a[1]], [O[2], a[2]], 'r-', label=r'Vector $\vec{a}$')
ax.plot([O[0], b[0]], [O[1], b[1]], [O[2], b[2]], 'g-', label=r'Vector $\vec{b}$')
ax.plot([O[0], p[0]], [O[1], p[1]], [O[2], p[2]], 'b-', label=r'Vector $\vec{a}\times\vec{b}$')

ax.scatter(O[0], O[1], O[2], color='k', s=100)
ax.scatter(a[0], a[1], a[2], color='r', s=50)
ax.scatter(b[0], b[1], b[2], color='g', s=50)
ax.scatter(p[0], p[1], p[2], color='b', s=50)

ax.text(O[0] - 0.3, O[1] - 0.2, O[2], 'O (0,0,0)', color='k')
ax.text(a[0] + 0.1, a[1], a[2], f'({a[0]}, {a[1]}, {a[2]})', color='r')
ax.text(b[0] - 0.5, b[1], b[2], f'({b[0]}, {b[1]}, {b[2]})', color='g')
ax.text(p[0] + 0.1, p[1], p[2], f'({p[0]}, {p[1]}, {p[2]})', color='b')


ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('Plot')

ax.legend()
plt.grid(True)

ax.view_init(20,30)

plt.savefig("../figs/plot_p.jpg")
plt.show()
