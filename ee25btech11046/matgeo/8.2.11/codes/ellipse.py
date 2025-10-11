import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
import ctypes

ellipse = ctypes.CDLL('./ellipse.so')
ellipse.function.argtypes = [
    ctypes.c_double,
    ctypes.c_double
]
ellipse.function.restype = None

V = np.array([[1/100, 0], [0, 1/400]])
u = np.array([0, 0]).reshape(-1, 1)
f = -1

lam_raw, P_raw = LA.eig(V)

if lam_raw[0] > lam_raw[1]:
    lam = np.array([lam_raw[1], lam_raw[0]])
    P = P_raw[:, [1, 0]]
else:
    lam = lam_raw
    P = P_raw

e = np.sqrt(1 - lam[0] / lam[1])
O = -LA.inv(V) @ u
a = np.sqrt(-f / lam[0])
b = np.sqrt(-f / lam[1])
c = np.sqrt(a**2 - b**2)
# The major axis vector 'n' is the eigenvector for the smaller eigenvalue
n = P[:, 0].reshape(-1, 1)

ellipse.function(
    a,
    b
)

F1 = O + c * n
F2 = O - c * n
V1 = O + a * n
V2 = O - a * n
d = a / e
latus_rectum_length = 2 * b**2 / a

theta = np.linspace(0, 2 * np.pi, 200)
standard_ellipse = np.vstack((a * np.cos(theta), b * np.sin(theta)))
ellipse_points = P @ standard_ellipse + O

plt.figure(figsize=(12, 12))
plt.plot(ellipse_points[0, :], ellipse_points[1, :], label=r'$\frac{x^2}{100} + \frac{y^2}{400} = 1$')
plt.plot(F1[0], F1[1], 'go', label=fr'Foci ({F1[0,0]:.2f}, $\pm${F1[1,0]:.2f})')
plt.plot(F2[0], F2[1], 'go')
plt.plot(V1[0], V1[1], 'ro', label=fr'Vertices ({V1[0,0]:.1f}, $\pm${V1[1,0]:.1f})')
plt.plot(V2[0], V2[1], 'ro')
directrix1_y = O[1,0] + d
directrix2_y = O[1,0] - d
plt.axhline(y=directrix1_y, color='green', linestyle='-', label=fr'Directrix y=$\pm${directrix1_y:.2f}')
plt.axhline(y=directrix2_y, color='green', linestyle='-')

latus_x_coords = np.array([-latus_rectum_length / 2, latus_rectum_length / 2])
plt.plot(latus_x_coords, [F1[1,0], F1[1,0]], 'r-', lw=2, label=f'Latus Rectum = {latus_rectum_length:.2f}')
plt.plot(latus_x_coords, [F2[1,0], F2[1,0]], 'r-', lw=2)

plt.title("Ellipse")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(color='black')
plt.axvline(color='black')
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.savefig("../figs/plot_c.jpg")
plt.show()
