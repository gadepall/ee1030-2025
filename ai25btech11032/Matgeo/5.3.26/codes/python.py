import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ------------------------------
# Step 1: Solve for k using SymPy
# ------------------------------
k = sp.symbols('k')
expr = (-k + 7) / 2   # from row reduction condition
solution = sp.solve(sp.Eq(expr, 0), k)
k_val = float(solution[0])
print(f"Calculated k = {k_val}")

# ------------------------------
# Step 2: Build augmented matrix with NumPy
# ------------------------------
def augmented_matrix(k):
    return np.array([
        [2, 3, 7],
        [k-1, k+2, 3*k]
    ], dtype=float)

A = augmented_matrix(k_val)
print("\nOriginal Augmented Matrix:")
print(A)

# ------------------------------
# Step 3: Row reduction in NumPy
# ------------------------------
def row_reduce(A):
    A = A.astype(float).copy()
    if A[0,0] != 0:
        factor = A[1,0] / A[0,0]
        A[1,:] = A[1,:] - factor * A[0,:]
    return A

R = row_reduce(A)
print("\nRow Reduced Matrix:")
print(R)

# ------------------------------
# Step 4: Plot the single line
# ------------------------------
x_vals = np.linspace(-5, 5, 400)

# From (k-1)x+(k+2)y=3k or y = (3k-(k-1)x)/(k+2)
y_vals = (3*k_val - (k_val-1)*x_vals) / (k_val+2)

plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, label=rf"$2x+3y=7 = ({int(k_val)}-1)x+({int(k_val)}+2)y=3k$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.title(f"System of Equations (Infinite Solutions, k={k_val})")
plt.savefig("pyinfsols.png")
plt.show()

