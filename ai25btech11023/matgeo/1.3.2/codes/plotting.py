import numpy as np
import matplotlib.pyplot as plt

# Read coordinates from output.dat
coords = np.loadtxt('output.dat')
A, B, C, D = coords

def linegen(P, Q, num=100):
    return np.column_stack([
        np.linspace(P[0], Q[0], num),
        np.linspace(P[1], Q[1], num)
    ])

# Generate the sides of the parallelogram
AB = linegen(A, B)
BC = linegen(B, C)
CD = linegen(C, D)
DA = linegen(D, A)

# Plot the sides
plt.plot(AB[:, 0], AB[:, 1])
plt.plot(BC[:, 0], BC[:, 1])
plt.plot(CD[:, 0], CD[:, 1])
plt.plot(DA[:, 0], DA[:, 1])

# Scatter and label vertices correctly
for name, pt in zip(['A', 'B', 'C', 'D'], [A, B, C, D]):
    plt.scatter(pt[0], pt[1])
    plt.text(pt[0] + 0.05, pt[1] + 0.05, f'{name}{tuple(map(int, pt))}')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.title('Parallelogram ABCD')

plt.savefig('../figs/fig.png')
plt.show()

