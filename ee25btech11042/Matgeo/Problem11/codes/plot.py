import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Load the Shared C Library ---
# Assumes 'line_solver.so' is in the same directory.
try:
    line_lib = ctypes.CDLL('./5.8.39.so')
except OSError as e:
    print("Error: Could not load the shared library 'line_solver.so'.")
    print("Please ensure you have compiled 'line_solver.c' correctly.")
    print(e)
    exit()

# --- Define the C function's signature for Python ---
calculate_y_c = line_lib.calculate_y
calculate_y_c.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
calculate_y_c.restype = ctypes.c_double

# --- Define coefficients for BOTH equations ---
# Equation 1: 2x + 3y = 9
a1, b1, c1 = 2.0, 3.0, 9.0
# Equation 2: 4x + 6y = 18
a2, b2, c2 = 4.0, 6.0, 18.0

# --- Generate data points using the C function ---
x_values = np.linspace(0, 5, 100)
y_values_1 = []
y_values_2 = []

# Call the C function for each x value for both lines
for x in x_values:
    y1 = calculate_y_c(x, a1, b1, c1)
    y_values_1.append(y1)
    
    y2 = calculate_y_c(x, a2, b2, c2)
    y_values_2.append(y2)

# --- Plot the Results ---
plt.figure(figsize=(8, 6))

# Plot the first line
plt.plot(x_values, y_values_1, 
         label=f'{int(a1)}x + {int(b1)}y = {int(c1)} (via C)', 
         color='blue', 
         linewidth=2)

# Plot the second line on top with a different style
plt.plot(x_values, y_values_2, 
         label=f'{int(a2)}x + {int(b2)}y = {int(c2)} (via C)', 
         color='red', 
         linestyle='--', 
         linewidth=4)

plt.title('Plotting Two Identical Lines Using a C Function')
plt.xlabel('Cost of Pencil (x)')
plt.ylabel('Cost of Eraser (y)')
plt.grid(True)
plt.legend()
plt.show()

print("Plot generated successfully!")
