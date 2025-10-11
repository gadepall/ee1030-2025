import ctypes
import numpy as np
import matplotlib.pyplot as plt

solver_lib = ctypes.CDLL('./normal.so')


# Define the function signature (argument types and return type).
solve_func = solver_lib.solve_for_point
solve_func.argtypes = [
    ctypes.c_double, 
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
solve_func.restype = None

# Prepare variables for the C function call for the line 3x - 4y - 7 = 0.
line_A = ctypes.c_double(3.0)
line_B = ctypes.c_double(-4.0)
contact_x_ptr = ctypes.c_double()
contact_y_ptr = ctypes.c_double()

# Call the C function from Python.
solve_func(line_A, line_B, ctypes.byref(contact_x_ptr), ctypes.byref(contact_y_ptr))

# [cite_start]Get the results from the pointers, which corresponds to your correct calculation. [cite: 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526]
contact_x = contact_x_ptr.value
contact_y = contact_y_ptr.value

print("--- Python with C Library Solution ---")
print(f"The point of contact is ({contact_x:.1f}, {contact_y:.1f})")

# --- 2. Plotting ---
x_vals = np.linspace(0.1, 5, 400)
curve = x_vals + 1/x_vals
line = (3*x_vals - 7) / 4
# The normal passes through (contact_x, contact_y) and is perpendicular to the line.
# Slope of line is 3/4, so slope of normal is -4/3.
normal_line = (-4/3)*(x_vals - contact_x) + contact_y

plt.figure(figsize=(10, 8))
plt.plot(x_vals, curve, label='Curve: $y = x + 1/x$', color='blue')
plt.plot(x_vals, line, label='Line: $3x - 4y - 7 = 0$', color='red', linestyle='--')
plt.plot(x_vals, normal_line, label='Normal to Curve', color='green')
plt.scatter(contact_x, contact_y, color='black', zorder=5, label=f'Point of Contact ({contact_x:.1f}, {contact_y:.1f})')
plt.annotate(
    f'({contact_x:.1f}, {contact_y:.2f})',
    xy=(contact_x, contact_y),             
    xytext=(10, -15),                   
    textcoords='offset points'          
)
plt.title('Geometric Solution (via C Library on Linux)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.ylim(-1, 6)
plt.xlim(-1, 6)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/10.4.3/figs/figure1.png")
plt.show()
