import numpy as np
import matplotlib.pyplot as plt

n1 = np.array([2, 3]).T
c1 = 1
n2 = np.array([1, 2]).T
c2 = 3
n3 = np.array([5, -6]).T
c3 = 1

x = np.linspace(-10, 10, 1000)
for i in range(1, 4):
    y = (eval(f"c{i}") - eval(f"n{i}")[0] * x) / eval(f"n{i}")[1]
    plt.plot(x, y)

xx = np.linspace(-1.5, -1, 100)
yy = xx**2

plt.plot(xx, yy,color='red')

xx = np.linspace(1 / 2, 1, 100)
yy = xx**2

plt.plot(xx, yy,color='red')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("4.13.59")
plt.legend()
plt.grid(True)

plt.savefig("../figs/python.png")
plt.show()
