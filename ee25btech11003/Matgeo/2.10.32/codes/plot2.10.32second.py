import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load compiled C library
lib = np.ctypeslib.load_library("libcompute", ".")

# Declare the function type — this time no explicit POINTER usage
lib.computeRandS.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS")
]
lib.computeRandS.restype = None

# Prepare vectors as NumPy arrays
p = np.array([6.0, 0.0, 0.0], dtype=np.float64)
q = np.array([0.0, 9.0, 0.0], dtype=np.float64)
r = np.zeros(3, dtype=np.float64)
s = np.zeros(3, dtype=np.float64)

# Call the C function directly (no pointers!)
lib.computeRandS(p, q, r, s)

print("R =", r)
print("S =", s)

# --- Plotting (exact same as your code) ---
p_val = 6
q_val = 9  # satisfies 9*36 = 4*81

# Define points
O = np.array([0, 0])
P = np.array([p_val, 0])
Q = np.array([0, q_val])

# R divides PQ internally in ratio 2:3
R = (3*P + 2*Q) / 5

# S divides PQ externally in ratio 2:3
S = (3*P - 2*Q) / (3 - 2)   # formula for external division

# Plot points
points = {'O':O, 'P':P, 'Q':Q, 'R':R, 'S':S}

plt.figure(figsize=(6,6))
for name, pt in points.items():
    plt.scatter(pt[0], pt[1], label=name)
    plt.text(pt[0]+0.2, pt[1]+0.2, name, fontsize=12)

# Draw lines PQ, OR, OS
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'k--', label='PQ')
plt.plot([O[0], R[0]], [O[1], R[1]], 'r', label='OR')
plt.plot([O[0], S[0]], [O[1], S[1]], 'b', label='OS')

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Vectors OR and OS with OR ⟂ OS")
plt.show()

