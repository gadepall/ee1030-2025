import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3, -5],
              [6, -10]])
b = np.array([20, 40])

print("The system has no solution (inconsistent).")

x_vals = np.linspace(-10, 10, 400)

y1 = (3*x_vals - 20)/5

y2 = (6*x_vals - 40)/10

plt.figure(figsize=(6,6))
plt.plot(x_vals, y1, label=r'$3x - 5y = 20$')
plt.plot(x_vals, y2, '--', label=r'$6x - 10y = 40$ (same line)')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("System of Equations")
plt.legend()
plt.grid(True)
plt.savefig("/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/5.2.16/figs/Figure_1.png")
plt.show()
