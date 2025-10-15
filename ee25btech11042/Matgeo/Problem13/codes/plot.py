import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
import ctypes

# Load the compiled C shared library
ellipse = ctypes.CDLL('./8.2.5.so')
ellipse.function.argtypes = [
    ctypes.c_double,
    ctypes.c_double
]
ellipse.function.restype = None

# Define the matrix V for the ellipse x^2/9 + y^2/16 = 1
V = np.array([[1/9, 0], [0, 1/16]])
u = np.array([0, 0]).reshape(-1, 1)
f = -1

# Calculate eigenvalues and eigenvectors to find ellipse properties
lam_raw, P_raw = LA.eig(V)

# Sort eigenvalues to ensure lam[0] is the smaller one (for the major axis)
if lam_raw[0] > lam_raw[1]:
    lam = np.array([lam_raw[1], lam_raw[0]])
    P = P_raw[:, [1, 0]]
else:
    lam = lam_raw
    P = P_raw

e = np.sqrt(1 - lam[0] / lam[1])
O = -LA.inv(V) @ u
a = np.sqrt(-f / lam[0]) # Semi-major axis
b = np.sqrt(-f / lam[1]) # Semi-minor axis
c = np.sqrt(a**2 - b**2)
# The major axis vector 'n' is the eigenvector for the smaller eigenvalue
n = P[:, 0].reshape(-1, 1)

# Call the C function to print the properties
print("--- Properties from C function ---")
ellipse.function(
    a,
    b
)
print("--------------------------------")

# Calculate coordinates for plotting
F1 = O + c * n
F2 = O - c * n
V1 = O + a * n
V2 = O - a * n
d = a / e
latus_rectum_length = 2 * b**2 / a

# Generate points for the ellipse
theta = np.linspace(0, 2 * np.pi, 200)
standard_ellipse = np.vstack((b * np.cos(theta), a * np.sin(theta))) # Note: b with x, a with y for vertical ellipse standard form
ellipse_points = P @ standard_ellipse + O

# Plotting
plt.figure(figsize=(10, 12))
plt.plot(ellipse_points[0, :], ellipse_points[1, :], label=r'$\frac{x^2}{9} + \frac{y^2}{16} = 1$')
plt.plot(F1[0], F1[1], 'go', label=fr'Foci ({F1[0,0]:.2f}, $\pm${abs(F1[1,0]):.2f})')
plt.plot(F2[0], F2[1], 'go')
plt.plot(V1[0], V1[1], 'ro', label=fr'Vertices ({V1[0,0]:.1f}, $\pm${abs(V1[1,0]):.1f})')
plt.plot(V2[0], V2[1], 'ro')
directrix1_y = O[1,0] + d
directrix2_y = O[1,0] - d
plt.axhline(y=directrix1_y, color='black', linestyle='-', label=fr'Directrix y=$\pm${directrix1_y:.2f}')
plt.axhline(y=directrix2_y, color='black', linestyle='-')

latus_x_coords = np.array([-latus_rectum_length / 2, latus_rectum_length / 2])
plt.plot(latus_x_coords, [F1[1,0], F1[1,0]], 'm-', lw=2, label=f'Latus Rectum = {latus_rectum_length:.2f}')
plt.plot(latus_x_coords, [F2[1,0], F2[1,0]], 'm-', lw=2)

plt.title("Ellipse: $x^2/9 + y^2/16 = 1$")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline(color='black', linewidth=0.5)
plt.axvline(color='black', linewidth=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.savefig("Figure_1.png")
plt.show()
