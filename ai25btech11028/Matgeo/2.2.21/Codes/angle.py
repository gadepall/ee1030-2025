  import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./libline_angle.so")

# Define function signature
lib.find_other_slopes.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
lib.find_other_slopes.restype = ctypes.c_int

 def other_slopes_c(m1, theta):
    result = (ctypes.c_double * 2)()
    n = lib.find_other_slopes(m1, theta, result)
    return [result[i] for i in range(n)]

m1 = 0.5
theta = np.pi/4

slopes = other_slopes_c(m1, theta)
print("Slopes from C library:", slopes)

# --- Plotting ---
x = np.linspace(-10, 10, 100)

plt.axhline(0, color='k')
plt.axvline(0, color='k')

plt.plot(x, m1*x, 'r', label=f"Slope m1={m1}")
plt.plot(x, slopes[0]*x, 'g', label=f"Slope m2={slopes[0]:.2f}")
plt.plot(x, slopes[1]*x, 'b', label=f"Slope m2={slopes[1]:.2f}")

plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lines with given angle")

# Save before show
plt.savefig("/storage/emulated/0/matrix/Matgeo/2.2.21/figs/Figure_1.png", dpi=300, bbox_inches='tight')
plt.show()