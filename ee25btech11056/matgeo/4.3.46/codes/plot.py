import numpy as np
import matplotlib.pyplot as plt
import os 

#for generating figure in figs folder
figs_folder= os.path.join("..","figs")

# fixed value of k
k_val = 1

# line points
#parametric form of the given line
t = np.linspace(-5,5,200)

p = 2 + (-1)*t
q = (-3) + t
r = 1 + 6*t

# plane coefficients: 2x + y + z = 7
a, b, c, d = 2, 1, 1, 7

l = np.linspace(-10, 10, 100)
m = np.linspace(-10, 10, 100)
l, m = np.meshgrid(l, m)

n = (d - a * l - b * m) / c

# plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# line
ax.plot(p, q, r, label="line", color="red",linewidth=2)

# points
ax.scatter(1, -2, 7, color="black", s=5, label="P(1,-2,7)")
ax.scatter(3, -4, -5, color="green", s=5, label="A(3,-4,-5)")
ax.scatter(2, -3, 1, color="yellow", s=5, label="B(2,-3,1)")

# plane
ax.plot_surface(l, m, n, alpha=0.5, color="blue", edgecolor="none")

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Line and Plane")
ax.grid(True)
ax.legend()

plt.tight_layout()
fig.savefig(os.path.join(figs_folder,"intersection.png"))
plt.show()

