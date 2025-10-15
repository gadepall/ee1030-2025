import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

A=np.array([[2,5],[-4,3]],dtype=float)
b=np.array([2,-30], dtype=float)

x=np.linalg.solve(A,b)
print("Solution vector for the system of equations:",x)

x_vals = np.linspace(-2, 10, 400)

y1 = (2 - 2*x_vals) / 5
y2 = (4*x_vals - 30) / 3

plt.plot(x_vals, y1, label=r"$2x + 5y = 2$")
plt.plot(x_vals, y2, label=r"$-4x + 3y = -30$")

plt.scatter(x[0], x[1], color="red", zorder=5)
plt.text(x[0]+0.2, x[1], f"({x[0]:.1f}, {x[1]:.1f})", color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphical Solution of the Linear System")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(True)
plt.show()
