import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
lib = ctypes.CDLL("./code.so")

# Define argument types
lib.solve_intersection.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                   ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                   ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Prepare result variables
x_res = ctypes.c_double()
y_res = ctypes.c_double()

# Solve intersection for:
# 3x - 5y = 4   (a1=3, b1=-5, c1=4)
# 9x - 2y = 7   (a2=9, b2=-2, c2=7)
lib.solve_intersection(3, -5, 4, 9, -2, 7, ctypes.byref(x_res), ctypes.byref(y_res))

intersection = (x_res.value, y_res.value)

# Define lines for plotting
x = np.linspace(-5, 5, 400)
y1 = (3*x - 4)/5
y2 = (9*x - 7)/2

# Plot lines and intersection
plt.figure(figsize=(7, 7))
plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='red')

# Mark intersection
plt.scatter(*intersection, color='black')
plt.text(intersection[0]+0.5, intersection[1]-0.5,
         f'({intersection[0]:.2f}, {intersection[1]:.2f})',
         fontsize=10, color="black")

# Annotate equations
plt.text(2, (3*2 - 4)/5 + 1, "3x - 5y - 4 = 0", color="blue", fontsize=10)
plt.text(-4, (9*(-4) - 7)/2 + 2, "9x - 2y - 7 = 0", color="red", fontsize=10)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.title("Graph using C intersection function")
plt.show()

print("Intersection Point from C:", intersection)

