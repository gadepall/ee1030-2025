import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./libsection_int.so")

# Define argument and return types
lib.sectionFormula.argtypes = [
    ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
lib.sectionFormula.restype = None

# Values for a and b
a = 1
b = 0

# Points P and Q
P = (ctypes.c_double * 2)(2 * a, -3 * b)
Q = (ctypes.c_double * 2)(a, b)
R = (ctypes.c_double * 2)(0.0, 0.0)

# Ratio m:n
m, n = 3, 1

# Call the C function
lib.sectionFormula(m, n, P, Q, R)

# Convert to NumPy arrays for plotting
P_np = np.array([P[0], P[1]])
Q_np = np.array([Q[0], Q[1]])
R_np = np.array([R[0], R[1]])

print("Position vector of the point R (from C):", R_np)

# Plotting
plt.figure(figsize=(6, 6))
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Plot P, Q, and R
plt.scatter(*P_np, color='blue', label='P (2a, -3b)')
plt.scatter(*Q_np, color='green', label='Q (a, b)')
plt.scatter(*R_np, color='red', label=f'R (ratio {m}:{n})')

# Draw line between P and Q
plt.plot([P_np[0], Q_np[0]], [P_np[1], Q_np[1]], color='gray', linestyle='--')

# Annotate points
plt.text(P_np[0]+0.2, P_np[1]+0.2, 'P')
plt.text(Q_np[0]+0.2, Q_np[1]+0.2, 'Q')
plt.text(R_np[0]+0.2, R_np[1]+0.2, 'R')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Section Formula Visualization (Using C & Python)')
plt.legend()
plt.grid(True)
plt.axis('equal')

# Save the plot
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/1.4.26/figs/q1.png")

# Show plot
plt.show()
