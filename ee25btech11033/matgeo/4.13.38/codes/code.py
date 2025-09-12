import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt
def plot_geometry(P, Q, R, S, point_parallel, line_coeffs):
    """
    Generates and displays a plot based on the calculated geometric data.
    """
    # Define triangle vertices
    triangle = [P, Q, R, P]
    triangle_x, triangle_y = zip(*triangle)

    # Define median line PS
    median_ps_x = [P[0], S[0]]
    median_ps_y = [P[1], S[1]]

    # Generate points for the parallel line using its equation: ax + by + c = 0
    x_vals = np.linspace(-2, 10, 100)
    a, b, c = line_coeffs
    
    # Avoid division by zero for vertical lines (where b=0)
    if abs(b) > 1e-9:
        y_vals = (-a * x_vals - c) / b
    else:
        # For a vertical line, x is constant
        x_vals = np.full_like(x_vals, -c / a)
        y_vals = np.linspace(-3, 5, 100)

    # Create the plot
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot the geometry
    ax.plot(triangle_x, triangle_y, 'b-', label='Triangle PQR', linewidth=2)
    ax.plot(median_ps_x, median_ps_y, 'g--', label='Median PS', linewidth=2)
    ax.plot(x_vals, y_vals, 'r-', label=f'Parallel Line ({a:.0f}x + {b:.1f}y + {c:.1f} = 0)', linewidth=2)

    # Plot and label the points
    points = {f'P{P}': P, f'Q{Q}': Q, f'R{R}': R, f'S({S[0]:.1f},{S[1]:.1f})': S, f'{point_parallel}': point_parallel}
    for label, (x, y) in points.items():
        ax.plot(x, y, 'ko', markersize=8)
        ax.text(x + 0.2, y + 0.2, label, fontsize=12)

    # Format the plot
    ax.set_title('Plot Generated from C Function Calculations', fontsize=16)
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)
    ax.legend(fontsize=12)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')
    plt.xlim(-1, 10)
    plt.ylim(-3, 5)
    plt.savefig('../figs/fig2.png')
    plt.show()




# --- Step 1: Load the shared C library ---


plot_lib = ctypes.CDLL("./code.so")

# --- Step 2: Define the C function signature for ctypes ---
# This tells Python what argument types the C function expects and what it returns.
calculate_plot_values = plot_lib.calculate_plot_values
calculate_plot_values.argtypes = [
    ctypes.c_double, ctypes.c_double,  # px, py
    ctypes.c_double, ctypes.c_double,  # qx, qy
    ctypes.c_double, ctypes.c_double,  # rx, ry
    ctypes.c_double, ctypes.c_double,  # ppx, ppy
    ctypes.POINTER(ctypes.c_double),   # out_sx
    ctypes.POINTER(ctypes.c_double),   # out_sy
    ctypes.POINTER(ctypes.c_double),   # out_a
    ctypes.POINTER(ctypes.c_double),   # out_b
    ctypes.POINTER(ctypes.c_double)    # out_c
]
calculate_plot_values.restype = None

# --- Step 3: Prepare data and call the C function ---
# Define input points for the calculation.
P = (2.0, 2.0)
Q = (6.0, -1.0)
R = (7.0, 3.0)
point_on_parallel_line = (1.0, -1.0)

# Prepare output variables that the C function will write to.
sx = ctypes.c_double()
sy = ctypes.c_double()
a = ctypes.c_double()
b = ctypes.c_double()
c = ctypes.c_double()

# Call the C function with the inputs and pointers to the output variables.
calculate_plot_values(
    P[0], P[1],
    Q[0], Q[1],
    R[0], R[1],
    point_on_parallel_line[0], point_on_parallel_line[1],
    ctypes.byref(sx), ctypes.byref(sy),
    ctypes.byref(a), ctypes.byref(b), ctypes.byref(c)
)

# Retrieve the values from the ctypes objects.
S = (sx.value, sy.value)
line_coeffs = (a.value, b.value, c.value)

print(f"Calculated Midpoint S from C: ({S[0]:.1f}, {S[1]:.1f})")
print(f"Parallel Line Equation from C: {line_coeffs[0]:.1f}x + {line_coeffs[1]:.1f}y + {line_coeffs[2]:.1f} = 0")
print("(Note: This is equivalent to 2x + 9y + 7 = 0)")

# --- Step 4: Plot the results using matplotlib ---
plot_geometry(P, Q, R, S, point_on_parallel_line, line_coeffs)


