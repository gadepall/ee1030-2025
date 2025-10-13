import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libconic.so")  

lib.ellipse_eccentricity.restype = ctypes.c_double
lib.ellipse_eccentricity.argtypes = [ctypes.c_double, ctypes.c_double]

lib.hyperbola_eccentricity.restype = ctypes.c_double
lib.hyperbola_eccentricity.argtypes = [ctypes.c_double, ctypes.c_double]

lib.ellipse_focus.restype = ctypes.c_double
lib.ellipse_focus.argtypes = [ctypes.c_double, ctypes.c_double]

lib.hyperbola_focus.restype = ctypes.c_double
lib.hyperbola_focus.argtypes = [ctypes.c_double, ctypes.c_double]

a_e, b_e = 2, 1
a_h, b_h = np.sqrt(3), 1

e_e = lib.ellipse_eccentricity(a_e, b_e)
e_h = lib.hyperbola_eccentricity(a_h, b_h)
c_e = lib.ellipse_focus(a_e, b_e)
c_h = lib.hyperbola_focus(a_h, b_h)

print(f"Eccentricities: e_E={e_e:.3f}, e_H={e_h:.3f}, Product={e_e*e_h:.3f}")
print(f"Ellipse focus distance: {c_e:.3f}, Hyperbola focus distance: {c_h:.3f}")

theta = np.linspace(0, 2*np.pi, 400)
x_ellipse = a_e * np.cos(theta)
y_ellipse = b_e * np.sin(theta)
focus1 = (c_e, 0)
focus2 = (-c_e, 0)

x_h = np.linspace(-5, 5, 2000)
x_h = x_h[np.abs(x_h) >= a_h]
y_h = np.sqrt((x_h**2 / a_h**2 - 1) * b_h**2)
focus_h1 = (c_h, 0)
focus_h2 = (-c_h, 0)
x_f, y_f = focus1
lhs = x_f**2 / a_h**2 - y_f**2 / b_h**2
print("Hyperbola LHS at ellipse focus =", lhs)

plt.plot(x_ellipse, y_ellipse, label=r'Ellipse: $\frac{x^2}{4} + y^2 = 1$')
plt.plot(x_h, y_h, 'r', label=r'Hyperbola: $\frac{x^2}{3} - y^2 = 1$')
plt.plot(x_h, -y_h, 'r')

plt.scatter(*focus1, color='green', s=80, label='Ellipse Focus (+)')
plt.scatter(*focus2, color='green', s=80, label='Ellipse Focus (-)')
plt.scatter(*focus_h1, color='purple', s=80, label='Hyperbola Focus (+)')
plt.scatter(*focus_h2, color='purple', s=80, label='Hyperbola Focus (-)')

plt.gca().set_aspect('equal')
plt.legend(fontsize=8, loc="upper right")
plt.title(fr"Ellipse & Hyperbola ($e_E={e_e:.3f}, e_H={e_h:.3f}$)")
plt.grid(True)
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/8.4.16/figs/Figure_1.png")
plt.show()

