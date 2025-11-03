import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# folder to save figure
figs_folder = os.path.join("..", "figs")

# load shared object
lib = ctypes.CDLL("./points.so")

# define function signature
lib.solve_ab.argtypes = [
    ((ctypes.c_double * 2) * 2),  # V1
    (ctypes.c_double * 2),        # u1
    ctypes.c_double,              # f1
    ((ctypes.c_double * 2) * 2),  # V2
    (ctypes.c_double * 2),        # u2
    ctypes.c_double,              # f2
    (ctypes.c_double * 2)         # result
]
lib.solve_ab.restype = None

# define inputs
V1 = ((ctypes.c_double * 2) * 2)()
V2 = ((ctypes.c_double * 2) * 2)()
for i in range(2):
    V1[i][i] = 1.0
    V2[i][i] = 1.0

u1 = (ctypes.c_double * 2)(0.0, 0.0)  # (a/2,0) placeholder
u2 = (ctypes.c_double * 2)(0.0, 0.0)  # (b/2,0) placeholder
f1 = 6.0
f2 = -4.0

# result array
result = (ctypes.c_double * 2)()

# call C function
lib.solve_ab(V1, u1, f1, V2, u2, f2, result)
a, b = result[0], result[1]

print(f"Values from C: a = {a}, b = {b}, a+b = {a+b}")

# --- PLOTTING ---

# grid for plotting
x_vals = np.linspace(-15, 15, 400)
y_vals = np.linspace(-15, 15, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# implicit circle equations
F1 = X**2 + Y**2 + a*X + 6
F2 = X**2 + Y**2 + b*X - 4

# plot
fig, ax = plt.subplots(figsize=(6,6))

# plot contours (zero level set = circle)
ax.contour(X, Y, F1, levels=[0], colors="red", linewidths=2)
ax.contour(X, Y, F2, levels=[0], colors="blue", linewidths=2)

# mark intersection point P(1,2)
ax.scatter(1, 2, color="black")
ax.text(1+0.4, 2+0.2, "P(1,2)", fontsize=10, color="black")

# formatting
ax.set_aspect("equal")
ax.axhline(0, color="black", lw=0.8)
ax.axvline(0, color="black", lw=0.8)
ax.set_title(r"Orthogonal Circles with Intersection at $P(1,2)$")
ax.grid(True)

# save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "circles.png"))
plt.show()

