import math
import numpy as np
import matplotlib.pyplot as plt

# Line AB: y = x / sqrt(3)
x = np.arange(-5, 5, 0.1)
y = x / math.sqrt(3)

# Line N: two points
xn = np.array([3, 2])
yn = np.array([math.sqrt(3), 2*math.sqrt(3)])

fig, ax = plt.subplots()

# Plot the lines normally
ax.plot(x, y, lw=3, color='#FFFF00', label='$AB$')
ax.plot(xn, yn, lw=3, color='#00FF00', label='$N$')

# Add arrows on the lines using annotate (single or double arrow)
# Double-headed arrow for AB
ax.annotate('', xy=(x[-1], y[-1]), xytext=(x[0], y[0]),
            arrowprops=dict(arrowstyle='<->', color='#FFFF00', lw=3))

# Single-headed arrow for N
ax.annotate('', xy=(xn[1], yn[1]), xytext=(xn[0], yn[0]),
            arrowprops=dict(arrowstyle='->', color='#00FF00', lw=3))

# Labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Normal to a line")

# Grid and legend
ax.grid(True)
ax.legend()

plt.savefig("../Figs/norm.png")
plt.show()

