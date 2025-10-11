import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 15, 400)
y1 = x - 8
y2 = x - 16/3

plt.figure(figsize=(8, 6))
plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='red')
plt.text(10, 2, r'$x - y = 8$', color='blue', fontsize=12)
plt.text(10, 7, r'$3x - 3y = 16$', color='red', fontsize=12)

plt.title("Plot of the system of equations")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.show()
