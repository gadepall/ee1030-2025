import numpy as np
import matplotlib.pyplot as plt

roots = np.load('roots.npy')
cs = np.load('cs.npy')

x = np.linspace(-1, 4, 400)

plt.figure(figsize=(10, 7))

# Original lines
# Line 1: x - y + 1 = 0  => y = x + 1
y1 = x + 1
plt.plot(x, y1, label='Line 1: $x - y + 1=0$', color='blue')

# Line 2: 2x - 3y + 5 = 0 => y = (2x + 5)/3
y2 = (2*x + 5)/3
plt.plot(x, y2, label='Line 2: $2x - 3y + 5=0$', color='green')

# Required lines (Line 3 and Line 4)
for i in range(2):
    a = roots[i]
    c = cs[i]
    # Equation: a x + y = c => y = -a x + c
    y = -a * x + c
    plt.plot(x, y, label=f'Line {i+3}: $({a:.3f})x + y = {c:.3f}$', linestyle='--')


# Plot intersection point (2,3)
plt.scatter(2, 3, color='red', s=50, label='Intersection (2,3)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Lines passing through (2,3) at distance 7/5 from (3,2)')
plt.legend()
plt.grid(True)
plt.show()

