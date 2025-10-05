# plot.py
import numpy as np
import matplotlib.pyplot as plt
from call import get_points

pts = get_points()
O = pts[0:2]
A = pts[2:4]  # tangent intersection (4, 0)
P = pts[4:6]  # (1, sqrt(3))
T = pts[6:8]  # other tangent direction point
N = pts[8:10] # other normal direction point

# Draw circle
theta = np.linspace(0, 2*np.pi, 400)
xc = 2 * np.cos(theta)
yc = 2 * np.sin(theta)

plt.figure(figsize=(7,7))
plt.plot(xc, yc, 'k--', label='Circle $x^2 + y^2 = 4$')

# Plot the tangent (from A towards T)
tan_x = [A[0], T[0]]
tan_y = [A[1], T[1]]
plt.plot(tan_x, tan_y, 'tab:red', label="Tangent at $P$")

# Plot the normal (from O towards N)
norm_x = [O[0], N[0]]
norm_y = [O[1], N[1]]
plt.plot(norm_x, norm_y, 'tab:green', label="Normal at $P$")

# Draw triangle OAP
tri_x = [O[0], A[0], P[0], O[0]]
tri_y = [O[1], A[1], P[1], O[1]]
plt.plot(tri_x, tri_y, 'b-', alpha=0.7, label='Triangle OAP')

# Points
plt.scatter([O[0], A[0], P[0]], [O[1], A[1], P[1]], color='purple', zorder=5)
plt.text(O[0], O[1]-0.2, "O", fontsize=12)
plt.text(A[0]+0.1, A[1]-0.1, "A", fontsize=12)
plt.text(P[0]+0.1, P[1]+0.1, "P", fontsize=12)

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.title("Triangle formed by X axis, tangent, normal to $x^2 + y^2 = 4$ \n at $P(1,\\sqrt{3})$")
plt.show()

