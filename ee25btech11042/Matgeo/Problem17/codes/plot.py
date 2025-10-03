import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./9.2.2.so')

# Define the function signature
get_data_func = lib.get_conic_data
get_data_func.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS')]
get_data_func.restype = None

# Create a buffer and call the C function
output_array = np.zeros(16, dtype=np.double)
get_data_func(output_array)

# Unpack the data from C
V1 = output_array[0:4].reshape((2, 2))
u1 = output_array[4:6]
V2 = output_array[6:10].reshape((2, 2))
u2 = output_array[10:12]
solution_point1 = output_array[12:14]
solution_point2 = output_array[14:16]

# --- Plotting Code ---
a = 1.0 # Must match the value in the C code
x_vals = np.linspace(-8*a, 8*a, 800)
y_vals = np.linspace(-8*a, 8*a, 800)
X, Y = np.meshgrid(x_vals, y_vals)

# Equations for contour plotting
eq1 = V1[1,1]*Y**2 + 2*(u1[0]*X)
eq2 = V2[0,0]*X**2 + V2[1,1]*Y**2 - 16*a**2

plt.figure(figsize=(10, 10))
plt.contour(X, Y, eq1, levels=[0], colors='red')
plt.contour(X, Y, eq2, levels=[0], colors='blue')

# --- Shading the Region ---
# The region is where y^2 <= 6ax AND x^2 + y^2 <= 16a^2
# The intersection occurs at x = 2a
x_intersect = 2 * a

# Part 1: Under the parabola from x=0 to x=2a
x_fill_1 = np.linspace(0, x_intersect, 200)
y_fill_1_upper = np.sqrt(6 * a * x_fill_1)
y_fill_1_lower = -y_fill_1_upper
plt.fill_between(x_fill_1, y_fill_1_lower, y_fill_1_upper, color='gray', alpha=0.5, label='Region of Intersection')

# Part 2: Under the circle from x=2a to x=4a
x_fill_2 = np.linspace(x_intersect, 4 * a, 200)
y_fill_2_upper = np.sqrt(16 * a**2 - x_fill_2**2)
y_fill_2_lower = -y_fill_2_upper
plt.fill_between(x_fill_2, y_fill_2_lower, y_fill_2_upper, color='gray', alpha=0.5)

# Plot solution points
plt.plot(solution_point1[0], solution_point1[1], 'ko', markersize=8, label=f'Intersection 1 from C')
plt.plot(solution_point2[0], solution_point2[1], 'ko', markersize=8, label=f'Intersection 2 from C')

plt.title('Plot from C Shared Library Data', fontsize=16)
plt.xlabel('x-axis'); plt.ylabel('y-axis')
plt.grid(True, linestyle='--'); plt.axhline(0, color='k', lw=0.5); plt.axvline(0, color='k', lw=0.5)
plt.gca().set_aspect('equal', adjustable='box'); plt.xlim(-5*a, 5*a); plt.ylim(-5*a, 5*a)
plt.legend()
plt.savefig('so_python_plot.png')
print("Plot saved to so_python_plot.png")
plt.show()
