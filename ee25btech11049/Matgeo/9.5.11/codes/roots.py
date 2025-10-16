import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

# --- 1. SETUP CTYPES TO INTERFACE WITH THE C LIBRARY ---

# Define the name of the shared library based on the OS
if os.name == 'nt': # Windows
    lib_name = 'roots.dll'
else: # Linux, macOS, etc.
    lib_name = 'roots.so'

# Find the full path to the library in the current directory
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_name)

# Load the shared library
try:
    solver_lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading shared library: {e}")
    print("Please make sure you have compiled solver.c into a shared library.")
    exit()

# Define the argument types and return type for the NEW C function
# void solve_conic_intersection(double* V, double* u, double f, double* h, double* m, double* kappa1, double* kappa2)
solve_conic_c = solver_lib.solve_conic_intersection
solve_conic_c.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                          ctypes.c_double,
                          ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
solve_conic_c.restype = None


# --- 2. SOLVE FOR THE ROOTS USING THE C MATRIX FUNCTION ---

# Define conic parameters for 9x^2 - 155x - y - 500 = 0
V = np.array([[9, 0], [0, 0]], dtype=np.float64)
u = np.array([-155/2, -1/2], dtype=np.float64)
f = -500.0

# Define line parameters for the x-axis (y=0)
h = np.array([0, 0], dtype=np.float64)
m = np.array([1, 0], dtype=np.float64)

# Create ctypes variables to hold the results
root1_c = ctypes.c_double()
root2_c = ctypes.c_double()

# Convert numpy arrays to the ctypes pointers C expects
V_p = V.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
u_p = u.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
h_p = h.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
m_p = m.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call the C function
solve_conic_c(V_p, u_p, f, h_p, m_p, ctypes.byref(root1_c), ctypes.byref(root2_c))

# Extract the Python float values
roots = np.array([root1_c.value, root2_c.value])

print("--- Root Calculation (from C using Matrix Theory) ---")
print(f"The roots (kappa values) are: x1 = {roots[0]:.4f} and x2 = {roots[1]:.4f}\n")


# --- 3. GENERATE THE PLOT ---
# This part remains the same, as it just visualizes the results.
a, b, c = 9.0, -155.0, -500.0

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
x_vals = np.linspace(-10, 30, 500)
y_vals = a*x_vals**2 + b*x_vals + c
ax.plot(x_vals, y_vals, label=f'$y = {int(a)}x^2 + {int(b)}x + {int(c)}$')
ax.axhline(0, color='orange', linewidth=1.5)

sorted_roots = np.sort(roots)
roots_y = np.zeros_like(sorted_roots)
point_labels = ['B', 'A']
colors = ['gold', '#9400D3']

ax.scatter(sorted_roots, roots_y, c=colors, s=50, zorder=5, edgecolor='black')

for i in range(len(sorted_roots)):
    label = f"$\\mathbf{{{point_labels[i]}}}$\\n({sorted_roots[i]:.2f}, {roots_y[i]:.0f})"
    ax.annotate(label, (sorted_roots[i], roots_y[i]), textcoords="offset points",
                xytext=(0, 15), ha='center', fontsize=10, fontweight='bold')

ax.grid(True)
ax.legend(loc='lower left')
ax.set_title('Parabola with x-intercepts (solved with C Matrix)', fontsize=16)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-15, 35)
ax.set_ylim(-1250, 250)

print("--- Plot Generation ---")
print("Displaying plot...")
plt.show()


