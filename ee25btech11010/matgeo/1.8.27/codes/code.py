import ctypes
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# =======================
# Load C shared library
# =======================
lib = ctypes.CDLL("./code.so")

# Define argument and return types
lib.solveSphere.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
lib.solveSphere.restype = None

# Prepare output variables
Cx = ctypes.c_double()
Cy = ctypes.c_double()
Cz = ctypes.c_double()
R  = ctypes.c_double()

# Call the C function (k=10 inside C)
lib.solveSphere(ctypes.byref(Cx), ctypes.byref(Cy), ctypes.byref(Cz), ctypes.byref(R))

# Extract results from C
cx, cy, cz, r = Cx.value, Cy.value, Cz.value, R.value

if r < 0:
    print("No real sphere exists for k=10")
    exit()

print(f"Equation of sphere (from C): (x - {cx:.2f})^2 + (y - {cy:.2f})^2 + (z - {cz:.2f})^2 = {r**2:.2f}")
print(f"Center: ({cx:.2f}, {cy:.2f}, {cz:.2f}), Radius: {r:.2f}")

# =======================
# Plotting (Matplotlib)
# =======================
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
X = cx + r * np.outer(np.cos(u), np.sin(v))
Y = cy + r * np.outer(np.sin(u), np.sin(v))
Z = cz + r * np.outer(np.ones_like(u), np.cos(v))

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, color='cyan', alpha=0.5, edgecolor='k', linewidth=0.3)
ax.scatter([cx], [cy], [cz], color='red', s=50, label="Center")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Sphere locus: PA² + PB² = 2k² (k=10, from C)")
ax.legend()

plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/1.8.27/figs/fig1.png")

plt.show()
