import ctypes
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# --- 1. Load the C Shared Library ---
# The shared library must be in the same directory as this script.
# We are now directly loading 'libsolver.so'.
c_lib = ctypes.CDLL('./libsolver.so')


# --- 2. Define the Function Signature for ctypes ---
# This tells Python what argument types the C function expects and what it returns.
c_lib.solve_system.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double, # a1, b1, c1
    ctypes.c_double, ctypes.c_double, ctypes.c_double, # a2, b2, c2
    ctypes.POINTER(ctypes.c_double), # pointer to x_result
    ctypes.POINTER(ctypes.c_double)  # pointer to y_result
]
c_lib.solve_system.restype = ctypes.c_int


# --- 3. Prepare Inputs from the Hostel Problem ---
# Equation 1: 1*x + 25*y = 4500
a1, b1, c1 = 1.0, 25.0, 4500.0
# Equation 2: 1*x + 30*y = 5200
a2, b2, c2 = 1.0, 30.0, 5200.0

print("Solving the system:")
print(f"Equation 1: {a1}x + {b1}y = {c1}")
print(f"Equation 2: {a2}x + {b2}y = {c2}\n")


# --- 4. Call the C Function ---
# Create pointers for the C function to write the results into.
x_result = ctypes.c_double()
y_result = ctypes.c_double()

result_code = c_lib.solve_system(a1, b1, c1, a2, b2, c2, ctypes.byref(x_result), ctypes.byref(y_result))


# --- 5. Process and Display the Numerical Solution ---
if result_code == 0:
    fixed_charge = x_result.value
    cost_per_day = y_result.value
    print("--- Numerical Solution (from C code) ---")
    print(f"The fixed monthly charge (x) is: ₹{fixed_charge:.2f}")
    print(f"The cost of food per day (y) is: ₹{cost_per_day:.2f}\n")
else:
    print("The C function indicated that no unique solution exists.")
    fixed_charge, cost_per_day = None, None # No solution to plot


# --- 6. Plot the Graphical Solution ---
if fixed_charge is not None:
    
    # Create the plot
    plt.figure(figsize=(10, 8))
    
    # --- MODIFICATION: Set plot boundaries and extend lines ---
    # Define the viewing window for the plot
    plt.xlim(0, 2200)
    plt.ylim(0, 200)
    
    # Create x-values that span the entire width of the plot
    x_vals = np.array(plt.xlim())

    # Calculate corresponding y-values for each equation
    # from y = (c - ax) / b
    y_vals1 = (c1 - a1 * x_vals) / b1
    y_vals2 = (c2 - a2 * x_vals) / b2
    
    # Plot the two lines
    plt.plot(x_vals, y_vals1, label=f'{a1}x + {b1}y = {c1}')
    plt.plot(x_vals, y_vals2, label=f'{a2}x + {b2}y = {c2}')
    
    # Plot the intersection point
    plt.plot(fixed_charge, cost_per_day, 'ro', markersize=8, label=f'Solution')
    
    # --- MODIFICATION: Add annotation for the intersection point ---
    annotation_text = f'({fixed_charge:.0f}, {cost_per_day:.0f})'
    plt.annotate(annotation_text,
                 xy=(fixed_charge, cost_per_day),
                 xytext=(fixed_charge + 50, cost_per_day + 5), # Offset the text slightly
                 fontsize=12)

    # --- MODIFICATION: Removed the title ---
    plt.xlabel('Fixed Charge (x)', fontsize=12)
    plt.ylabel('Cost per Day (y)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Save the plot to a file before showing it
    plt.savefig("/home/shriyasnh/Desktop/matgeonew/5.9.7/figs/hostel_charges_plot.png")
    
    # Show the plot
    plt.show()

