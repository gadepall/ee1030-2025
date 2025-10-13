from sympy import symbols,solve
import numpy as np
import matplotlib.pyplot as plt
import math

x, y = symbols('x y')

eq1 = y**2 - 4*x
eq2 = x**2 + y**2 - 6*x + 1
solutions = solve([eq1, eq2], (x, y))

print("Solutions:")
for sol in solutions:
    print(f"x = {sol[0]}, y = {sol[1]}")

Y = np.linspace(-10,10,50)
p = Y*Y/4
l = Y - 1

fig = plt.figure(figsize = (6,6))
ax = fig.add_subplot(111)

ax.plot(p,Y, label='(1)')
ax.plot(l,Y, label = '$y=x+1$')
circle = plt.Circle((3, 0), math.sqrt(8), color='green', fill=False, linewidth=2, label = '(2)')
ax.add_patch(circle)
ax.scatter(1,2, label='(1,2)', color = 'red')

ax.grid(True)
plt.legend()
plt.show()

