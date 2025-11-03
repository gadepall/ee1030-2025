import numpy as np
import matplotlib.pyplot as plt


y = np.linspace(-4, 4, 400)
x = y**2 / 4

xt = np.linspace(0, 3, 100)
yt = xt + 1

plt.plot(x, y, 'g', linewidth=1.5)
plt.plot(xt, yt, 'black', linewidth=1.2)
plt.scatter(1, 2, color='red', zorder=5)

plt.text(1.1, 2, "P(1,2)", fontsize=9)
plt.text(2, 3.5, "Parabola", color='g', fontsize=9)
plt.text(1.6, 2.7, "Tangent", color='black', fontsize=9)

plt.axhline(0, color='gray', linewidth=0.8)
plt.axvline(0, color='gray', linewidth=0.8)

plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(False)

plt.savefig("../figs/img2.png", dpi=300, bbox_inches='tight')
plt.close()

