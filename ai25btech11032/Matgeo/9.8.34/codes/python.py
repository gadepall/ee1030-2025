import numpy as np
import matplotlib.pyplot as plt

# Circles:
# C1: 3x^2 + 3y^2 - 2x + 12y - 9 = 0
a1 = 3.0
u1 = np.array([-1.0, 6.0])
f1 = -9.0

# C2: x^2 + y^2 + 6x + 2y - 15 = 0
a2 = 1.0
u2 = np.array([3.0, 1.0])
f2 = -15.0

# ---- Find radical axis (line through intersections) ----
mu = -a1/a2
L = 2*(u1 + mu*u2)   # vector
c = f1 + mu*f2       # scalar

print("Line (raw):", L, "· x +", c, "= 0")

# Scale to nice integers
L = -0.5*L
c = -0.5*c
print("Final line:", f"({int(L[0])} \\\\ {int(L[1])})^T x {int(c):+d} = 0")

# ---- Plot circles and line ----
theta = np.linspace(0, 2*np.pi, 400)

# Circle 1
center1 = -u1/a1
r1 = np.sqrt((u1@u1)/(a1*a1) - f1/a1)
x1 = center1[0] + r1*np.cos(theta)
y1 = center1[1] + r1*np.sin(theta)

# Circle 2
center2 = -u2/a2
r2 = np.sqrt((u2@u2)/(a2*a2) - f2/a2)
x2 = center2[0] + r2*np.cos(theta)
y2 = center2[1] + r2*np.sin(theta)

# Line points
xx = np.linspace(min(center1[0]-r1, center2[0]-r2)-1,
                 max(center1[0]+r1, center2[0]+r2)+1, 600)
yy = (-c - L[0]*xx)/L[1]

plt.plot(x1, y1, label="C1")
plt.plot(x2, y2, label="C2")
plt.plot(xx, yy, label="Radical axis")
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(); plt.grid(True)
plt.savefig("newradical.png")
plt.show()

