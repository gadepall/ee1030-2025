import numpy as np
import matplotlib.pyplot as plt
import ctypes

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ + O)
	return x_circ

tangent = ctypes.CDLL('./tangent.so')
tangent.function.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
tangent.function.restype = None

def get_points_from_c(r, d):
    q1_x, q1_y = ctypes.c_double(0), ctypes.c_double(0)
    q2_x, q2_y = ctypes.c_double(0), ctypes.c_double(0)
    tangent.function(
        r,
        d,
        ctypes.byref(q1_x),
        ctypes.byref(q1_y),
        ctypes.byref(q2_x), 
        ctypes.byref(q2_y)
    )
    return np.array([q1_x.value, q1_y.value]), np.array([q2_x.value, q2_y.value])

r, d = 2.5, 7.0
q1, q2 = get_points_from_c(r, d)
center = np.array([0, 0]).reshape(-1, 1)
P = np.array([d, 0])

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
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.axhline()
plt.axvline()
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.savefig("../figs/plot_c.jpg")
plt.show()
