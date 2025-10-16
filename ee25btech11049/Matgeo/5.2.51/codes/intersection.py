import ctypes
import numpy as np
import matplotlib.pyplot as plt
from libs.funcs import line_dir_pt, param_norm

# --- Ctypes setup to call the C function ---

# Load the shared library.
# NOTE: You must compile solver.c into a shared library first.
# On Linux/macOS, use: gcc -shared -o solver.so -fPIC solver.c
try:
    solver_lib = ctypes.CDLL('./intersection.so')
except OSError:
    print("Error: Could not find 'solver.so'.")
    print("Please compile the C code first using: gcc -shared -o solver.so -fPIC solver.c")
    exit()


# Define the function signature from the C code.
solve_system_c = solver_lib.solve_system
solve_system_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
solve_system_c.restype = None

# --- Solving the system of equations ---

# The first equation is 5x + 2y = 4
a, b, e = 5.0, 2.0, 4.0

# The second equation is 7x + 3y = 5
c, d, f = 7.0, 3.0, 5.0

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
print(f"5*({x_sol}) + 2*({y_sol}) = {5*x_sol + 2*y_sol}")
print(f"7*({x_sol}) + 3*({y_sol}) = {7*x_sol + 3*y_sol}")

# Normal vectors for plotting
n1 = np.array([[a], [b]])
c1 = e
n2 = np.array([[c], [d]])
c2 = f

# Generate points for the first line
m1, A1 = param_norm(n1, c1)
line1_pts = line_dir_pt(m1, A1, -10, 10)

# Generate points for the second line
m2, A2 = param_norm(n2, c2)
line2_pts = line_dir_pt(m2, A2, -10, 10)

# Plot the lines
plt.plot(line1_pts[0,:], line1_pts[1,:], label='5x + 2y = 4')
plt.plot(line2_pts[0,:], line2_pts[1,:], label='7x + 3y = 5')

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

