import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.suptitle("Q 4.4.36")

plt.rcParams['text.usetex'] = True

# x/a + y/b = 1
# => y = b(1 - x/a)

a = 2
b = 6

x_in = np.array([a, 0])
y_in = np.array([0, b])

ax.axline(x_in, y_in, color="blue", label=f"Arbitrary line $\\frac{{x}}{{{a}}} + \\frac{{y}}{{{b}}} = 1$")

ax.plot(*x_in, "ro")
ax.plot(*y_in, "ro")

ax.fill_between(
    np.linspace(0, a, 100),
    0,
    b * (1 - np.linspace(0, a, 100) / a),
    color="cyan",
    label="Area of triangle",
)

ax.annotate("A", x_in, textcoords="offset points", xytext=(0, 10), ha="center")
ax.annotate("B", y_in, textcoords="offset points", xytext=(10, 0), ha="center")
ax.annotate("O", (0, 0), textcoords="offset points", xytext=(-10, -15), ha="center")

ax.annotate(
    "a",
    (a/2, -0.5),
    textcoords="offset points",
    xytext=(0,-15),
    ha="center",
    va='bottom',
    arrowprops=dict(
        arrowstyle=f"-[, widthB={0.5*a}, lengthB=0.2",
        lw=1.5,
        color="red",
    ),
    fontsize=12,
    color="blue",
)

ax.annotate(
    "b",
    (-0.5, b/2),
    textcoords="offset points",
    xytext=(-10,-5.3),
    ha="center",
    va='bottom',
    arrowprops=dict(
        arrowstyle=f"-[, widthB={0.6*b}, lengthB=0.2",
        lw=1.5,
        color="red",
    ),
    fontsize=12,
    color="blue",
)

ax.grid()
ax.legend()
ax.set_xticks(np.arange(-8, 9, 2))
ax.set_yticks(np.arange(-8, 9, 2))
ax.axhline(0, color="black", lw=1)
ax.axvline(0, color="black", lw=1)
ax.set_aspect("equal")


ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# plt.show()
fig.savefig("../figs/plot.png", dpi=300)
