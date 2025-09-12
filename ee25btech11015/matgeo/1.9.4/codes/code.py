import numpy as np
import matplotlib.pyplot as plt
import ctypes
import os

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL('./code.so')
except OSError:
    print("Error: 'code.so' not found.")
    print("Please compile code.c using: gcc -shared -o code.so -fPIC code.c")
    exit()

# Define argument and return types for the C function
c_lib.norm_lambda_a.argtypes = [ctypes.c_float, ctypes.c_float]
c_lib.norm_lambda_a.restype = ctypes.c_float

# --- Given ---
norm_a = 4.0
lam_min, lam_max = -3.0, 2.0

# --- Generate λ values and call C function ---
lambdas = np.linspace(lam_min, lam_max, 200)
y = np.array([c_lib.norm_lambda_a(ctypes.c_float(l), ctypes.c_float(norm_a)) for l in lambdas])

# --- Range ---
y_min, y_max = np.min(y), np.max(y)
print(f"✅ The values of ||λa|| lie in the interval [{y_min:.0f}, {y_max:.0f}]")

# --- Plotting ---
plt.plot(lambdas, y, label="||λa|| = 4|λ|", color="blue")

# Mark endpoints
plt.scatter([lam_min, lam_max],
            [c_lib.norm_lambda_a(lam_min, norm_a), c_lib.norm_lambda_a(lam_max, norm_a)],
            color=['red','green'], zorder=5)

# Labels
plt.text(lam_min, c_lib.norm_lambda_a(lam_min, norm_a)+0.5,
         f"({lam_min:.0f},{c_lib.norm_lambda_a(lam_min, norm_a):.0f})")
plt.text(lam_max, c_lib.norm_lambda_a(lam_max, norm_a)+0.5,
         f"({lam_max:.0f},{c_lib.norm_lambda_a(lam_max, norm_a):.0f})")

# Axes and grid
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.xlabel("lambda")
plt.ylabel("||lambda a||")
plt.title("Graph of ||lambda a|| = 4|lambda|")
plt.legend(loc='best')
ptl.
plt.grid(True)
plt.show()