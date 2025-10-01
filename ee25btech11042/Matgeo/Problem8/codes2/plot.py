# plot_from_so.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./5.2.44.so')

# Define the function signature
get_data_func = lib.get_conic_data
get_data_func.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS')]
get_data_func.restype = None

# Create a buffer and call the C function
output_array = np.zeros(14, dtype=np.double)
get_data_func(output_array)

# Unpack the data from C
V1 = output_array[0:4].reshape((2, 2))
u1 = output_array[4:6]
V2 = output_array[6:10].reshape((2, 2))
u2 = output_array[10:12]
solution_point = output_array[12:14]

# --- Plotting Code ---
x_vals = np.linspace(-10, 15, 500)
y_vals = np.linspace(-10, 15, 500)
X, Y = np.meshgrid(x_vals, y_vals)

eq1 = V1[0,0]*X**2 + V1[1,1]*Y**2 + 2*(u1[0]*X + u1[1]*Y)
eq2 = V2[0,0]*X**2 + V2[1,1]*Y**2 + 2*(u2[0]*X + u2[1]*Y)

plt.figure(figsize=(10, 10))
plt.contour(X, Y, eq1, levels=[0], colors='red')
plt.contour(X, Y, eq2, levels=[0], colors='blue')
plt.plot(x_vals, (2/3)*x_vals, 'g--', label='Common Chord')
plt.plot(solution_point[0], solution_point[1], 'ko', markersize=10, label=f'Solution from C: ({solution_point[0]}, {solution_point[1]})')

plt.title('Plot from C Shared Library Data', fontsize=16)
plt.xlabel('x-axis'); plt.ylabel('y-axis')
plt.grid(True, linestyle='--'); plt.axhline(0, color='k', lw=0.5); plt.axvline(0, color='k', lw=0.5)
plt.gca().set_aspect('equal', adjustable='box'); plt.xlim(-5, 10); plt.ylim(-5, 10)
plt.legend()
plt.savefig('so_python_plot.png')
print("Plot saved to so_python_plot.png")
plt.show()
