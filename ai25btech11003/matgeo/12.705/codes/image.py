import numpy as np
import matplotlib.pyplot as plt


# (x-1)^2 = (y - 3)

t = np.linspace(-5,5, 10000)
y = 3 + t*t/4
x1 = 1 + t/2

fig, ax = plt.subplots()

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.plot(x1,y, c="b", label=f"$y=x^2 -2x + 4$")
ax.plot(t,3*t/t, c="r", ls="--", label="y=3")

ax.scatter(1,3, c="g", edgecolor="k", marker="8", zorder=5, s=50)
ax.text(1, 2.93, "P(1,3)", fontweight="bold", fontsize=11, va="top")

ax.grid(True)
ax.legend(loc="upper right")
ax.set_aspect("equal")

ax.set_xlim(-2,5)
ax.set_ylim(2,9)


plt.tight_layout
plt.savefig("fig1.png")
plt.show()
