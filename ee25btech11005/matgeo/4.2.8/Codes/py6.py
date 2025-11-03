import numpy as np
import matplotlib.pyplot as plt

x_val = 2.5
y_vals = np.linspace(-5, 5, 200)
x_vals = np.full_like(y_vals, x_val)

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, 'b-', linewidth=2)

plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)

plt.title("Line: 2x - 5 = 0 (x = 2.5)")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axis("equal")
plt.grid(True)
plt.show()

