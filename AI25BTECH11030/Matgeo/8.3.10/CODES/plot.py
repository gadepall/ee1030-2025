import numpy as np
import matplotlib.pyplot as plt

e, D = 5 / 8, 10
l = D * (1 - e ** 2) / e
a = D / (2 * e)
b = a * np.sqrt(1 - e ** 2)
c = a * e
print("The length of latus rectum is: ",l)
t = np.linspace(0, 2 * np.pi, 1000)
x, y = a * np.cos(t), b * np.sin(t)

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, y, 'b-', lw=2, label='Ellipse')

ax.scatter([c, -c], [0, 0], color='r', s=50, label='Foci $F_1, F_2$')
ax.text(c + .2, 0.3, f'$F_1({c}, 0)$')
ax.text(-c - .2, 0.3, f'$F_2({-c}, 0)$')

ax.plot([-a, a], [0, 0], 'k--', alpha=.5)
ax.plot([0, 0], [-b, b], 'k--', alpha=.5)

ax.text(a + .3, 0, f'$A({a}, 0)$')
ax.text(-a - .9, 0, f'$A\'(-{a}, 0)$')
ax.text(0.3, b + .3, f'$B(0, {b:.2f})$')
ax.text(0.3, -b - .5, f'$B\'(0, -{b:.2f})$')

ax.plot([c, c], [-l / 2, l / 2], 'g', lw=3, label='Latus rectum')
ax.plot([-c, -c], [-l / 2, l / 2], 'g', lw=3)
ax.text(c + .2, l / 2, f'$\\ell = {l:.2f}$')
ax.text(-c - 1.0, l / 2, f'$\\ell = {l:.2f}$')

ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-8, 8)
ax.set_title(f'Ellipse $e={e}$,  $D={D}$\n$\\ell = {l} = 39/4$')
ax.grid(alpha=.3)
ax.legend()
plt.tight_layout()
plt.savefig("fig1.png")
plt.show()
