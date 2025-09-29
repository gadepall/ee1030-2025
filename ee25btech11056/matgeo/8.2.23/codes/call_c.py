import ctypes
import os
import sys #to make the code interact with the interpreter and its runtime environment
import numpy as np
import matplotlib.pyplot as plt

# save figure in figs folder
figs_folder = os.path.join("..", "figs")

# load shared object
lib = ctypes.CDLL("./points.so")

# define argument and return types
lib.ellipse.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # c
    ctypes.POINTER(ctypes.c_double),  # e
    ctypes.POINTER(ctypes.c_double),  # f1
    ctypes.POINTER(ctypes.c_double),  # f2
    ctypes.POINTER(ctypes.c_double),  # vert
    ctypes.POINTER(ctypes.c_double)   # n
]
lib.ellipse.restype = None

# inputs
f1 = (ctypes.c_double * 2)(0.0, 5.0)
f2 = (ctypes.c_double * 2)(0.0, -5.0)
vert = (ctypes.c_double * 2)(0.0, 13.0)
vert2 = (ctypes.c_double * 2)(0.0, -13.0)
 

# outputs (initialized to zero)
c = ctypes.c_double(0.0)
e = ctypes.c_double(0.0)
n = (ctypes.c_double * 2)(0.0, 0.0)

# call C function
lib.ellipse(ctypes.byref(c), ctypes.byref(e), f1, f2, vert, n) #byref to pass pointer to variable(its address)

# get results
c_val = c.value  #to access the numerical value of c
e_val = e.value
n_val = [n[i] for i in range(2)]  #stor index 0 and 1 of n array

print("c (directrix constant):", c_val)
print("e (eccentricity):", e_val)
print("n (normal vector):", n_val)

# ===== Ellipse equation (x^2 / a^2 + y^2 / b^2 = 1) =====
b = vert[1]   # semi-major axis (along y-axis)
c_f = f1[1]   # distance to focus from origin
a = np.sqrt(b**2 - c_f**2)  # semi-minor axis (along x-axis)

x_vals = np.linspace(-a, a, 400)
y_upper = b * np.sqrt(1 - (x_vals**2 / a**2)) # x**2 means x^2
y_lower = -y_upper

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(x_vals, y_upper, 'r')  #r means red line,just straight line
ax.plot(x_vals, y_lower, 'r', label="Ellipse")

# plot foci
ax.scatter([f1[0], f2[0]], [f1[1], f2[1]], color="blue", label="Foci")
ax.text(f1[0] + 0.5, f1[1], f"F1{tuple(f1)}", fontsize=10, color="blue")
ax.text(f2[0] + 0.5, f2[1], f"F2{tuple(f2)}", fontsize=10, color="blue")

# plot vertex
ax.scatter([vert[0]], [vert[1]], color="green", label="Vertex1")
ax.text(vert[0] + 0.5, vert[1], f"B1{tuple(vert)}", fontsize=10, color="green")

ax.scatter([vert2[0]], [vert2[1]], color="orange", label="Vertex2")
ax.text(vert2[0] + 0.5, vert2[1], f"B2{tuple(vert2)}", fontsize=10, color="orange") #tuple to write the coordinates of vertex


# center axes
ax.axhline(0, color='black', linewidth=1) #draws x axes line at y=0 
ax.axvline(0, color='black', linewidth=1) #draws y axes line at x=0

# formatting
ax.set_aspect('equal') #make one unit on x the same as one unit on y , make equal units(scale for x and y)
ax.set_title("Ellipse")
ax.legend()
ax.grid(True)

# save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "ellipse.png"))
plt.show()

