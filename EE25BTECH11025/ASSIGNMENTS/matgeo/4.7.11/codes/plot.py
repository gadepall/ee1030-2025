import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(-10, 10, 100)
b = (3*a)/2 - (5/2)

A = np.linspace(-10, 10, 100)
B = (-3*A)/2 + (5/2)

x = [10/6, 10/6]
y = [15, -15]

X = [-15, 15]
Y = [0, 0]

plt.plot(a, b, 'r-')
plt.plot(A, B, 'r-')
plt.plot(x, y, 'k-')
plt.plot(X, Y, 'k-')

plt.text(10, 12.3, "3x-2y=5", fontsize=10, color='black')
plt.text(-8.3, 15, "3x+2y=5", fontsize=10, color='black')
plt.text(15.2, -0.06, "y=0", fontsize=10, color='black')
plt.text(1.6, 14.6, "x=10/6", fontsize=10, color='black')


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.grid(True)
plt.savefig("../figs/plot.png")
plt.show()