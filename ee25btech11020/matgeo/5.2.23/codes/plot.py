import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(-10, 10, 400)

y1 = (3*xx + 4)/5            # 3x - 5y = -4
y2 = (13 - 2*xx)/3           # 2x + 3y = 13

x_sol, y_sol = 53/19, 47/19

plt.figure(figsize=(6,6))
plt.plot(xx, y1, color="blue")
plt.plot(xx, y2, color="green")

plt.text(5, (3*5+4)/5, "3x - 5y = -4", color="blue")
plt.text(5, (13-2*5)/3, "2x + 3y = 13", color="green")

plt.scatter([x_sol], [y_sol], color="red")
plt.text(x_sol+0.2, y_sol, f"({x_sol:.2f}, {y_sol:.2f})", color="red")

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True)
plt.savefig("../figs/img2.png")

