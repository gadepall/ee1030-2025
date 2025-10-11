import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./liblineutils.so")

# Define argument/return types
lib.norm.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.norm.restype = ctypes.c_double

lib.normalize.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.normalize.restype = None

lib.compute_p.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double]
lib.compute_p.restype = ctypes.c_double

# Input data
n = np.array([np.sqrt(3), 1.0], dtype=np.double)
c = 2.0

# Allocate output for unit normal
unit_n = np.zeros(2, dtype=np.double)

# Convert numpy array to C pointer
n_ptr = n.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
unit_ptr = unit_n.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call C functions
norm_val = lib.norm(n_ptr)
lib.normalize(n_ptr, unit_ptr)
p_val = lib.compute_p(n_ptr, c)

print("||n|| =", norm_val)
print("Unit normal =", unit_n)
print("p =", p_val)

# ----------------- Plotting -----------------
# Line: sqrt(3)x + y + 2 = 0  => y = -sqrt(3)x - 2
x_vals = np.linspace(-4, 4, 200)
y_vals = -np.sqrt(3)*x_vals - 2

# Call C functions
norm_val = lib.norm(n_ptr)
lib.normalize(n_ptr, unit_ptr)
p_val = lib.compute_p(n_ptr, c)

print("||n|| =", norm_val)
print("Unit normal =", unit_n)
print("p =", p_val)

# ----------------- Plotting -----------------
# Line: sqrt(3)x + y + 2 = 0  => y = -sqrt(3)x - 2
x_vals = np.linspace(-4, 4, 200)
y_vals = -np.sqrt(3)*x_vals - 2
# Normal vector (scaled for plotting)
origin = np.array([0,0])
normal_line = np.vstack([origin, unit_n*2])  # scale for visibility

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, label=r"$\sqrt{3}x+y+2=0$")
plt.quiver(0,0, unit_n[0], unit_n[1], angles='xy', scale_units='xy', scale=1, color='red', label="Unit normal")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.gca().set_aspect("equal")
plt.title("Line and its Normal")
plt.grid(True)
plt.savefig("normalform.png")
plt.show()

