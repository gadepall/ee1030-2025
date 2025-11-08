import math
import numpy as np
import matplotlib.pyplot as plt

# Line AB: y = x / sqrt(3)
x = np.arange(-3, 5, 0.1)
y = x / math.sqrt(3)

# Original normal line N: two points
xn = np.array([3, 2])
yn = np.array([math.sqrt(3), 2*math.sqrt(3)])

# New line M: two points
xm = np.array([3, 4])
ym = np.array([math.sqrt(3), 0])

# Create 1 row, 2 columns of subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# --- Left subplot: AB and original N ---
ax = axs[0]
ax.plot(x, y, lw=3, color='#FF00FF', label='$AB$')
ax.plot(xn, yn, lw=3, color='#FF0000', label='$N$')
ax.annotate('', xy=(x[-1], y[-1]), xytext=(x[0], y[0]),
            arrowprops=dict(arrowstyle='<->', color='#FF00FF', lw=3))
ax.annotate('', xy=(xn[1], yn[1]), xytext=(xn[0], yn[0]),
            arrowprops=dict(arrowstyle='->', color='#FF0000', lw=3))
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("AB and N")
ax.grid(True)
ax.legend()
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 5)

# --- Right subplot: AB and new M ---
ax = axs[1]
ax.plot(x, y, lw=3, color='#FF00FF', label='$AB$')
ax.plot(xm, ym, lw=3, color='#0000FF', label='$M$')  # blue color for M
ax.annotate('', xy=(x[-1], y[-1]), xytext=(x[0], y[0]),
            arrowprops=dict(arrowstyle='<->', color='#FF00FF', lw=3))
ax.annotate('', xy=(xm[1], ym[1]), xytext=(xm[0], ym[0]),
            arrowprops=dict(arrowstyle='->', color='#0000FF', lw=3))
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("AB and M")
ax.grid(True)
ax.legend()
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 5)

plt.tight_layout()
plt.savefig("../Figs/normal.png")
plt.show()

