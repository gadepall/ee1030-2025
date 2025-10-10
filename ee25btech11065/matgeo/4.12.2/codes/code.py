import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# --- 1. C Library Setup ---

# Attempt to load the shared library.
try:
    # The name of the .so file should match the one compiled from your C code.
    c_lib = ctypes.CDLL('./solver.so')
except OSError:
    print("Error: 'solver.so' not found.")
    print("Please compile the 'solver.c' file from the Canvas first.")
    print("Command: gcc -shared -o solver.so -fPIC solver.c")
    exit()

# Define the return type of the C function.
c_lib.solve_for_k.restype = ctypes.c_double


# --- 2. Call C Function and Print Results ---

# Call the function from the C library to get the value of k.
k_value = c_lib.solve_for_k()
print(f"The C function calculated the value of k for which there is no solution:")
print(f"  k = {k_value:.2f}")


# --- 3. Prepare for Plotting ---

# Define a range of x values for the plot.
x = np.linspace(-5, 5, 100)

# Equation 1: 3x + y = 1  =>  y = 1 - 3x
y1 = 1 - 3 * x

# Equation 2: (2k - 1)x + (k - 1)y = 2k + 1
# Substitute the calculated value of k.
# (2*2 - 1)x + (2 - 1)y = 2*2 + 1  =>  3x + y = 5  =>  y = 5 - 3x
y2 = (2 * k_value + 1 - (2 * k_value - 1) * x) / (k_value - 1)


# --- 4. Plotting ---

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$3x + y = 1$')
plt.plot(x, y2, label=f'${{{(2*k_value-1):.0f}}}x + {{{(k_value-1):.0f}}}y = {{{(2*k_value+1):.0f}}}$ (for k={k_value:.0f})', linestyle='--')

# --- 5. Formatting the Plot ---

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(f'Lines for k = {k_value:.2f} (No Solution)', fontsize=14)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

