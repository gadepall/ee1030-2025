import numpy as np
import matplotlib.pyplot as plt


c = np.array([-1, -1])
p = np.array([1, 0])

def diam_opposite(center, point):
    return 2*center - point


def distance(pt1, pt2):
    return np.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)


q = diam_opposite(c, p)
r = distance(c, p)

print("The point Q is:", q)
print("Radius r:", r)

theta = np.linspace(0, 2*np.pi, 200)
circle_x = c[0] + r*np.cos(theta)
circle_y = c[1] + r*np.sin(theta)


fig, ax = plt.subplots()
ax.plot(circle_x, circle_y, color="blue", label="Circle")
ax.scatter([p[0], q[0]], [p[1], q[1]], color="red", label="Diameter Points")
ax.scatter(c[0], c[1], color="blue", marker="x", s=100, label="Center")
ax.plot([p[0], q[0]], [p[1], q[1]], "g--", label="Diameter")


ax.text(c[0], c[1], f"C({c[0]}, {c[1]})", fontsize=12, color="blue", ha="right", va="bottom")
ax.text(p[0], p[1], f"P({p[0]}, {p[1]})", fontsize=12, color="red", ha="left", va="top")
ax.text(q[0], q[1], f"Q({q[0]}, {q[1]})", fontsize=12, color="red", ha="right", va="top")

ax.set_aspect("equal", adjustable="datalim")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend(loc="upper right")
ax.grid(True)

plt.savefig("/Users/bhargavkrish/Desktop/BackupMatrix/ee25btech11013/matgeo/7.4.20/figs/Figure_1.png")  
plt.show()

