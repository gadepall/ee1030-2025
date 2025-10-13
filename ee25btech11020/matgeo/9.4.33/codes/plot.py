import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

a, b, c = 1, -4, 3

x = np.linspace(0, 4, 400)
y = a*x**2 + b*x + c

plt.figure(figsize=(6,4))
plt.plot(x, y, 'g', linewidth=2)
plt.axhline(0, color='black', linewidth=1)

roots = [1, 3]
plt.scatter(roots, [0, 0], color='black', zorder=5)
plt.text(1, 0.2, '(1,0)', ha='center', fontsize=9)
plt.text(3, 0.2, '(3,0)', ha='center', fontsize=9)

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

Path("../figs").mkdir(parents=True, exist_ok=True)
plt.savefig("../figs/img2.png", dpi=300, bbox_inches='tight')
plt.close()

