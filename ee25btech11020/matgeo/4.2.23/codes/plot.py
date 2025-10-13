import numpy as np
import matplotlib.pyplot as plt

line1 = np.array([2.0, 3.0, 1.0])
line2 = np.array([3.0, -2.0, 3.0])

x = np.linspace(-30, 30, 800)

y1 = -(line1[0]*x + line1[2]) / line1[1]
y2 = -(line2[0]*x + line2[2]) / line2[1]

plt.figure(figsize=(8,8))

plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="green")

mid = len(x)//2
plt.text(x[mid], y1[mid], f"{line1[0]}x + {line1[1]}y + {line1[2]} = 0",
         color="blue", fontsize=10, backgroundcolor="white")
plt.text(x[mid], y2[mid], f"{line2[0]}x + {line2[1]}y + {line2[2]} = 0",
         color="green", fontsize=10, backgroundcolor="white")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlim(-30, 30)
plt.ylim(-30, 30)

plt.grid(True)

plt.savefig("../figs/img1.png", dpi=300, bbox_inches="tight")


