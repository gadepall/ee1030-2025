
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 400)

x = t**2 + t + 1
y = t**2 - t + 1

plt.figure(figsize=(6,6))
plt.plot(x, y, color='red')

vx, vy = 1, 1
fx, fy = 1.25, 1.25

plt.scatter(vx, vy, color='red', s=60, zorder=3)
plt.scatter(fx, fy, color='green', s=60, zorder=3)


plt.grid(True)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Parametric Curve: x = t² + t + 1, y = t² - t + 1', fontsize=14)

plt.savefig('../figs/img2.png', dpi=300, bbox_inches='tight')
plt.close()

