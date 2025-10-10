import numpy as np
import matplotlib.pyplot as plt
import ctypes   # ✅ included

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL('./line.so')
except OSError:
    print("❌ Error: 'line.so' not found. Compile using: gcc -shared -o line.so -fPIC line_vectors.c")
    exit()

# Define argument and return types
c_lib.line_vectors.argtypes = [ctypes.POINTER(ctypes.c_float),
                               ctypes.POINTER(ctypes.c_float),
                               ctypes.POINTER(ctypes.c_float),
                               ctypes.POINTER(ctypes.c_float)]
c_lib.line_vectors.restype = None

# --- Prepare ctypes variables ---
dx = ctypes.c_float()
dy = ctypes.c_float()
nx = ctypes.c_float()
ny = ctypes.c_float()

# --- Call C function ---
c_lib.line_vectors(ctypes.byref(dx), ctypes.byref(dy), ctypes.byref(nx), ctypes.byref(ny))

print(f" Direction vector: ({dx.value}, {dy.value})")
print(f" Normal vector: ({nx.value}, {ny.value})")

# --- Plot the line y = x - 2 ---
x = np.linspace(-2, 6, 100)
y = x - 2

fig, ax = plt.subplots()
ax.plot(x, y, label="Line: y = x - 2", color="black")

# --- Choose a point on the line ---
P = np.array([2, 0], dtype=float)

# Plot direction vector
ax.arrow(P[0], P[1], dx.value, dy.value, 
         head_width=0.2, color="red", length_includes_head=True, label="Direction Vector")

# Plot normal vector
ax.arrow(P[0], P[1], nx.value, ny.value, 
         head_width=0.2, color="blue", length_includes_head=True, label="Normal Vector")

# Formatting
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Line y = x - 2 with Direction & Normal Vectors")
ax.legend()
ax.grid(True)
ax.set_aspect("equal")

plt.show()
