import ctypes
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# save figure in figs folder
figs_folder = os.path.join("..", "figs")
os.makedirs(figs_folder, exist_ok=True)  # create folder if it doesn't exist

# load the shared object
lib = ctypes.CDLL("./points.so")

# define return type and arg type
lib.gaussian_elimination.restype = ctypes.POINTER(ctypes.c_double)
lib.gaussian_elimination.argtypes = [((ctypes.c_double * 3) * 2)]

# define augmented matrix for father-son problem
# -3x + y = 3
# -2x + y = 13
a = ((ctypes.c_double * 3) * 2)()
a[0][:] = [-3.0, 1.0, 3.0]
a[1][:] = [-2.0, 1.0, 13.0]

# call the C function
sol = lib.gaussian_elimination(a)
solution = [sol[i] for i in range(2)]
x, y = solution
print("Solution from C:", solution)

# create x range for plotting
x_vals = np.linspace(0, 15, 100)

# equations solved for y
y1 = 3 * x_vals + 3       # from y = 3x + 3
y2 = 2 * x_vals + 13  # from y + 3 = 2(x+3)+10 → y = 2x + 13

# plotting
plt.figure(figsize=(8, 6))

# plot the lines
plt.plot(x_vals, y1, label="y = 3x + 3", color="green")
plt.plot(x_vals, y2, label="y = 2x + 13", color="blue")

# plot the solution point
plt.scatter(x, y, color="red", label=f"P({x:.2f},{y:.2f})")
plt.text(x + 0.3, y + 0.3, f"P({x:.2f},{y:.2f})", fontsize=10, color="red")

# labels and grid
plt.xlabel("X axis (Son's Age)")
plt.ylabel("Y axis (Father's Age)")
plt.title("Father-Son Age Problem: Intersection Point")
plt.legend()
plt.grid(True)

# save figure
plt.tight_layout()
plt.savefig(os.path.join(figs_folder, "solution.png"))
plt.show()

