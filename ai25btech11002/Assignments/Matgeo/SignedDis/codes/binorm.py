import math
import numpy as np
import matplotlib.pyplot as plt

# Line AB: y = x / sqrt(3)
x = np.arange(-5, 5, 0.1)
y = x / math.sqrt(3)

# Line N: two points
xn = np.array([3, 2])
yn = np.array([math.sqrt(3), 2*math.sqrt(3)])

# Line N: two points
xm = np.array([3, 4])
ym = np.array([math.sqrt(3), 0])

fig, ax = plt.subplots()

# Plot the lines normally
ax.plot(x, y, lw=3, color='#FF00FF', label='$AB$')
ax.plot(xn, yn, lw=3, color='#0000FF', label='$N$')
ax.plot(xm, ym, lw=3, color='#FF0000', label='$M$')

# Add arrows on the lines using annotate (single or double arrow)
# Double-headed arrow for AB
ax.annotate('', xy=(x[-1], y[-1]), xytext=(x[0], y[0]),
            arrowprops=dict(arrowstyle='<->', color='#FF00FF', lw=3))

# Single-headed arrow for N
ax.annotate('', xy=(xn[1], yn[1]), xytext=(xn[0], yn[0]),
            arrowprops=dict(arrowstyle='->', color='#0000FF', lw=3))

# Single-headed arrow for M
ax.annotate('', xy=(xm[1], ym[1]), xytext=(xm[0], ym[0]),
            arrowprops=dict(arrowstyle='->', color='#FF0000', lw=3))

# Labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Possibilities for normal to a line")

# Grid and legend
ax.grid(True)
ax.legend()

plt.savefig("../Figs/binorm.png")
plt.show()
