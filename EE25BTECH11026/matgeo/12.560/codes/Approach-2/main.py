import ctypes
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Load C library
lib = ctypes.CDLL("./libnormal.so")

# Define function signature: void normal_vector(double, double, double*)
lib.normal_vector.argtypes = (ctypes.c_double, ctypes.c_double,
                              np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"))

# Input point (3,4)
x0, y0 = 3.0, 4.0

# Allocate result array
result = np.zeros(2, dtype=np.float64)

# Call C function
lib.normal_vector(x0, y0, result)

# Convert to Sympy Matrix for column vector display
normal_vec = sp.Matrix(result)
print("Normal direction vector:")
sp.pprint(normal_vec)

# ---- Plotting ----
theta = np.linspace(0, 2*np.pi, 400)
circle_x = 5 * np.cos(theta)
circle_y = 5 * np.sin(theta)

plt.plot(circle_x, circle_y, label='Circle: x^2+y^2=25')
plt.plot(x0, y0, 'ro', label='Point (3,4)')
plt.quiver(x0, y0, result[0], result[1], angles='xy', scale_units='xy', scale=1,
           color='g', label='Normal vector')

plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/12.560/figs/Figure_2.png")
plt.show()

