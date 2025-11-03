import ctypes
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Load the C shared library
lib = ctypes.CDLL("./row_reduction.so")
lib.row_reduce.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=2, flags="C_CONTIGUOUS")
]

def row_reduce(matrix):
    A = np.array(matrix, dtype=np.float64, order='C')
    lib.row_reduce(A)
    return A

# ------------------------------
# Step 1: Solve for k using SymPy
# ------------------------------
k = sp.symbols('k')

# Row reduction condition: (-k+7)/2 = 0
expr = (-k + 7) / 2
solution = sp.solve(sp.Eq(expr, 0), k)
k_val = float(solution[0])   # numeric value for plotting

print(f"Calculated k = {k_val}")

# ------------------------------
# Step 2: Build augmented matrix with that k
# ------------------------------
A = np.array([
    [2, 3, 7],
    [k_val-1, k_val+2, 3*k_val]
], dtype=np.float64)

print("\nOriginal Augmented Matrix:")
print(A)

# ------------------------------
# Step 3: Row reduction via C
# ------------------------------
reduced = row_reduce(A.copy())
print("\nRow Reduced Matrix:")
print(reduced)

# ------------------------------
# Step 4: Plot only the single line
# ------------------------------
x_vals = np.linspace(-5, 5, 400)

# General second equation: (k-1)x+(k+2)y=3k or y = (3k-(k-1)x)/(k+2)
y = (3*k_val - (k_val-1)*x_vals) / (k_val+2)

plt.figure(figsize=(6,6))
plt.plot(x_vals, y, label=rf"$2x+3y=7 = ({int(k_val)}-1)x+({int(k_val)}+2)y=3k$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.title(f"System of Equations (Infinite Solutions, k={k_val})")
plt.savefig("infsols.png")
plt.show()

