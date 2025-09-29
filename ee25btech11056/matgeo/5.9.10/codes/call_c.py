import ctypes
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# save figure in figs folder
figs_folder = os.path.join("..", "figs")

# load the shared object
lib = ctypes.CDLL("./points.so")

# define return type and arg type
lib.gaussian_elimination.restype = ctypes.POINTER(ctypes.c_double)
lib.gaussian_elimination.argtypes = [((ctypes.c_double * 3) * 2)]

# define augmented matrix for equations
# 3x - y = 6  -> [3, -1, 6]
# 2x - y = -1 -> [2, -1, -1]
a = ((ctypes.c_double * 3) * 2)()
a[0][:] = [3.0, -1.0, 6.0]
a[1][:] = [2.0, -1.0, -1.0]

# call the C function
sol = lib.gaussian_elimination(a)
solution = [sol[i] for i in range(2)]
x, y = solution
print("Solution from C:", solution)

# create x range for plotting
x_vals = np.linspace(-10, 10, 100)

# equations
y1 = 3 * x_vals - 6      # from 3x - y = 6  → y = 3x - 6
y2 = 2 * x_vals + 1      # from 2x - y = -1 → y = 2x + 1

# plotting
plt.figure(figsize=(8, 6))

# plot the lines
plt.plot(x_vals, y1, label="3x - y = 6", color="green")
plt.plot(x_vals, y2, label="2x - y = -1", color="blue")

# plot the solution point
plt.scatter(x, y, color="red",label="P(7,15)")
plt.text(x + 0.5, y + 0.5, f"P({x:.2f},{y:.2f})", fontsize=10, color="red")

# labels and grid
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Intersection of Two Lines and Solution Point P")
plt.legend()
plt.grid(True)

# save figure
plt.tight_layout()
plt.savefig(os.path.join(figs_folder, "solution.png"))
plt.show()

