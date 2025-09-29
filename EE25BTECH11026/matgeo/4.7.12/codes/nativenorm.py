import math
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")


# -----------------------------
# Data
# -----------------------------
P = (4.0, 1.0) # given point
m_dir = -1.0 # slope for 135° direction (tan 135° = -1)
d = (-1.0, 1.0) # unit direction up to scale


# Given line: 4x - y = 0 -> y = 4x
# Parametric line through P in direction d: (x, y) = P + t d = (4 - t, 1 + t)
# Intersect with y = 4x:
# 1 + t = 4(4 - t) -> 1 + t = 16 - 4t -> 5t = 15 -> t = 3


t = 3.0
Q = (P[0] + t*d[0], P[1] + t*d[1]) # (1, 4)


# Distance along the 135° direction
DX = Q[0] - P[0]
DY = Q[1] - P[1]
distance = math.hypot(DX, DY) # 3*sqrt(2)


print(f"distance: {distance:.3f} units")


# -----------------------------
# Plot
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 6))


# Plot given line y = 4x
x_line = [ -1, 5 ]
y_line = [ 4*x for x in x_line ]
ax.plot(x_line, y_line, label='Line: 4x - y = 0 (y=4x)')


# Plot direction line through P (slope -1)
x_dir = [P[0] - 4, P[0] + 4]
y_dir = [P[1] + 4, P[1] - 4]
ax.plot(x_dir, y_dir, linestyle='--', label='Direction 135° (slope -1)')


# Points P and Q
ax.plot(P[0], P[1], 'ro')
ax.annotate('P(4,1)', xy=P, xytext=(P[0]+0.2, P[1]-0.5))
ax.plot(Q[0], Q[1], 'mo')
ax.annotate(f'Q{Q}', xy=Q, xytext=(Q[0]+0.2, Q[1]+0.2))


# Segment PQ (the measured distance)
ax.plot([P[0], Q[0]], [P[1], Q[1]], 'r-', linewidth=2)


# Annotate distance directly above the segment
mid = ((P[0]+Q[0])/2, (P[1]+Q[1])/2)
ax.text(mid[0], mid[1]+0.3, f'distance = {distance:.3f}', ha='center', va='bottom', fontsize=10, color='red')


# Axes formatting
ax.set_aspect('equal', 'box')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, alpha=0.4)
ax.legend(loc='upper right')


# Set sensible limits around all geometry
xs = [-1, 5, P[0], Q[0]]
ys = [min(y_line), max(y_line), P[1], Q[1]]
ax.set_xlim(min(xs)-1, max(xs)+1)
ax.set_ylim(min(ys)-1, max(ys)+1)

plt.savefig("/home/user/Matrix/Matgeo_assignments/4.7.12/figs/Figure_1.png")
plt.show()
