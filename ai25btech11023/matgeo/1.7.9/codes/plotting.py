import numpy as np
import matplotlib.pyplot as plt

# Read coordinates from output.dat (plain numbers expected)
coords = np.loadtxt('output.dat')
A, B, C = coords
def linegen(P, Q, num=100):
    return np.column_stack([
        np.linspace(P, Q, num),
        np.linspace(P[1], Q[1], num)
    ])
AC = linegen(A, C)

plt.plot(AC[:, 0], AC[:, 1])

for name, pt in zip(['A', 'B', 'C'], [A, B, C]):
    plt.scatter(pt[0], pt[1])
    plt.text(pt[0]+0.05, pt[1]+0.05, f'{name}{tuple(map(int, pt))}')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.title('A,B and C are collinear')
plt.savefig('../figs/fig.png')
plt.show()

