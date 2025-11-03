import numpy as np
import matplotlib.pyplot as plt

P = np.array([2, 6])
B = np.array([3, -1])
A = 2*P - B

radius = np.linalg.norm(B - P)
theta = np.linspace(0, 2*np.pi, 300)
x_circle = P[0] + radius*np.cos(theta)
y_circle = P[1] + radius*np.sin(theta)

plt.plot(x_circle, y_circle, 'r', label='Circle') 
plt.plot([A[0], B[0]], [A[1], B[1]], 'g--', label='Diameter')

plt.scatter([A[0], B[0], P[0]], [A[1], B[1], P[1]], color='blue')
plt.text(A[0], A[1]-0.5, f'A{tuple(A)}')
plt.text(B[0], B[1]+0.5, f'B{tuple(B)}')
plt.text(P[0]+0.2, P[1], f'P{tuple(P)}')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

#  Legend moved to top-right corner
plt.legend(loc="upper right")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Circle with Diameter AB and Center P")
plt.savefig("fig1.png")
plt.show()