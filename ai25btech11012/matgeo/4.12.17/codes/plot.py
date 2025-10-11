import numpy as np
import matplotlib.pyplot as plt

# Define lines: y - sqrt(3)|x| = 2
x = np.linspace(-6, 6, 400)
y1 = 2 + np.sqrt(3)*x    # y - sqrt(3)x = 2
y2 = 2 - np.sqrt(3)*x    # y + sqrt(3)x = 2

# Intersection point
I = np.array([0, 2])

# Points P1, P2
P1 = np.array([2.5, 2 + (5*np.sqrt(3))/2])
P2 = np.array([-2.5, 2 - (5*np.sqrt(3))/2])

# Feet of perpendiculars on bisectors
# Internal bisector (x=0)
Q1 = np.array([0, P1[1]])
Q2 = np.array([0, P2[1]])

# External bisector (y=2)
R1 = np.array([P1[0], 2])
R2 = np.array([P2[0], 2])

# Plot the two lines
plt.plot(x, y1, 'b', label=r"$y-\sqrt{3}x=2$")
plt.plot(x, y2, 'g', label=r"$y+\sqrt{3}x=2$")

# Plot the bisectors
plt.axvline(0, color='r', linestyle='--', label="Internal bisector $x=0$")
plt.axhline(2, color='m', linestyle='--', label="External bisector $y=2$")

# Plot points
plt.scatter(*I, color='k', s=60, label="Intersection (0,2)")
plt.scatter(*P1, color='c', s=60, label=r"$P_1$")
plt.scatter(*P2, color='y', s=60, label=r"$P_2$")
plt.scatter(*Q1, color='r', marker='x', s=80, label=r"Foot from $P_1$ on $x=0$")
plt.scatter(*Q2, color='r', marker='x', s=80, label=r"Foot from $P_2$ on $x=0$")
plt.scatter(*R1, color='m', marker='x', s=80, label=r"Foot from $P_1$ on $y=2$")
plt.scatter(*R2, color='m', marker='x', s=80, label=r"Foot from $P_2$ on $y=2$")

# Labels and grid
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Angle Bisectors and Feet of Perpendiculars")
plt.legend(loc="best", fontsize=8)
plt.grid(True)
plt.axis("equal")
plt.savefig('/Users/unnathi/Documents/ee1030-2025/ai25btech11012/matgeo/4.12.17/figs/fig.png')
plt.show()

