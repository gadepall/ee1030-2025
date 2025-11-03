import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
lib = ctypes.CDLL("./line1.dll")

# Define argument types
lib.solve_intersection.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                   ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                   ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Prepare result variables
x_res = ctypes.c_double()
y_res = ctypes.c_double()

lib.solve_intersection(1/2,1/3, -1, 1, -1/3, 0, ctypes.byref(x_res), ctypes.byref(y_res))

intersection = (x_res.value, y_res.value)

# Define lines for plotting
x = np.linspace(-5, 5, 400)
y1 = (-x/2 - 1)*3
y2 = 3*x

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
plt.text(2, -5, "x/2+y/3 = -1", color="blue", fontsize=10)
plt.text(-4, -13, "x-y/3= 0", color="red", fontsize=10)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.title("Graph using C intersection function")
plt.show()

print("Intersection Point from C:", intersection)
