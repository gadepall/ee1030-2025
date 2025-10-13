import numpy as np
import matplotlib.pyplot as plt

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ + O)
	return x_circ

def calculate_contact_points(r, d):
    if d < r:
        return None, None # External point is inside the circle
    x_coord = r**2 / d
    y_coord_abs = (r / d) * np.sqrt(d**2 - r**2)
    q1 = np.array([x_coord, y_coord_abs])
    q2 = np.array([x_coord, -y_coord_abs])
    return q1, q2

r = 2.5
d = 7.0

q1, q2 = calculate_contact_points(r, d)

center = np.array([0, 0]).reshape(-1, 1)
P = np.array([d, 0]) # External point P

circle_points = circ_gen(center, r)

plt.figure(figsize=(10, 8))

plt.plot(circle_points[0, :], circle_points[1, :], 'b-', label=f'Circle (r={r})')
plt.plot([P[0], q1[0]], [P[1], q1[1]], 'r-', label='Tangents from P')
plt.plot([P[0], q2[0]], [P[1], q2[1]], 'r-')
plt.plot([q1[0], q2[0]], [q1[1], q2[1]], 'k--', label='Chord of Contact')

points_to_label = {
    'C (0, 0)': center.flatten(),
    f'P ({d},0)': P,
    f'$T_1$ ({q1[0]:.2f}, {q1[1]:.2f})': q1,
    f'$T_2$ ({q2[0]:.2f}, {q2[1]:.2f})': q2
}
offsets = {
    'C (0, 0)': (-0.8, 0.1),
    f'P ({d},0)': (0.2, 0.1),
    f'$T_1$ ({q1[0]:.2f}, {q1[1]:.2f})': (0.2, 0.1),
    f'$T_2$ ({q2[0]:.2f}, {q2[1]:.2f})': (0.2, -0.4)
}
for label, point in points_to_label.items():
    plt.scatter(point[0], point[1], s=50, color='black', zorder=5)
    plt.text(point[0] + offsets[label][0], point[1] + offsets[label][1], label, fontsize=12)
plt.scatter([], [], s=50, color='black')

plt.title('Construction of Circle and its Tangents')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline()
plt.axvline()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle=':')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.savefig("../figs/plot_p.jpg")
plt.show()
