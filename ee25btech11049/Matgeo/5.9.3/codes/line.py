import ctypes
import numpy as np
import matplotlib.pyplot as plt
from libs.funcs import line_dir_pt, param_norm

# --- Ctypes setup to call the C function ---

# Load the shared library.
# NOTE: You must compile the corresponding C file into a shared library first.
# On Linux/macOS, use: gcc -shared -o intersection.so -fPIC your_c_file.c
try:
    # The script was named intersection.py, so we assume the shared library
    # might be named intersection.so
    solver_lib = ctypes.CDLL('./line.so')
except OSError:
    print("Error: Could not find 'line.so'.")
    print("Please ensure the C code is compiled into a shared library named 'line.so'.")
    exit()


# Define the function signature from the C code.
solve_system_c = solver_lib.solve_system
solve_system_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
solve_system_c.restype = None

# --- Solving the system of equations ---

# The first equation is 5x + 4y = 9500
a, b, e = 5.0, 4.0, 9500.0

# The second equation is 4x + 3y = 7370
c, d, f = 4.0, 3.0, 7370.0

# Create pointers for the output variables x and y
x = ctypes.c_double()
y = ctypes.c_double()

# Call the C function to solve the system
solve_system_c(a, b, c, d, e, f, ctypes.byref(x), ctypes.byref(y))

# Get the Python values from the ctypes objects
x_sol, y_sol = x.value, y.value

print(f"The solution from the C library is:")
print(f"x = {x_sol}")
print(f"y = {y_sol}")


# --- Verification and Plotting ---

print("\nVerification:")
# Note: Due to floating-point precision, the result might be extremely close but not exactly the integer value.
print(f"5*({x_sol}) + 4*({y_sol}) = {5*x_sol + 4*y_sol}")
print(f"4*({x_sol}) + 3*({y_sol}) = {4*x_sol + 3*y_sol}")

# Normal vectors for plotting
n1 = np.array([[a], [b]])
c1 = e
n2 = np.array([[c], [d]])
c2 = f

# Generate points for the first line (widened range for visibility)
m1, A1 = param_norm(n1, c1)
line1_pts = line_dir_pt(m1, A1, -5000, 5000)

# Generate points for the second line (widened range for visibility)
m2, A2 = param_norm(n2, c2)
line2_pts = line_dir_pt(m2, A2, -5000, 5000)

# Plot the lines
plt.plot(line1_pts[0,:], line1_pts[1,:], label='5x + 4y = 9500')
plt.plot(line2_pts[0,:], line2_pts[1,:], label='4x + 3y = 7370')

# Plot the intersection point
plt.plot(x_sol, y_sol, 'o', markersize=8, label=f'Intersection ({x_sol:.2f}, {y_sol:.2f})')

# Draw x and y axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Add labels and title for clarity
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Intersection of Two Lines (Solved with C)")
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
