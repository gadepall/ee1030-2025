import numpy as np
import matplotlib.pyplot as plt
import ctypes

try:
    c_lib = ctypes.CDLL('./solver.so')
except OSError:
    print("Error: 'solver.so' not found.")
    print("Compile the 'solver.c' using:")
    print("gcc -shared -o solver.so -fPIC solver.c")
    exit()

c_lib.solve_for_k.restype = ctypes.c_double

k_value = c_lib.solve_for_k()
print(f"The C function calculated the value of k for which there is no solution:")
print(f"  k = {k_value:.2f}")

x = np.linspace(-5, 5, 100)
y1 = 1 - 3 * x
# Equation 2: (2k - 1)x + (k - 1)y = 2k + 1  =>  y = ((2k + 1) - (2k -1)*x) / (k - 1)
y2 = ((2 * k_value + 1) - (2 * k_value - 1) * x) / (k_value - 1)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$3x + y = 1$')
plt.plot(x, y2, label=fr'${{{2*k_value-1:.0f}}}x + {{{k_value-1:.0f}}}y = {{{2*k_value+1:.0f}}}$ (for $k={k_value:.2f}$)', linestyle='--')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(f'Lines for k = {k_value:.2f} (No Solution)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

