import ctypes
import os
import platform
import numpy as np
import matplotlib.pyplot as plt
import sys

# --- Part 1: Compile and Load the C Library ---

# Define the C source file and the name for the shared library
c_source_file = 'vertices.c'
lib_name = 'libvertices.so'
if platform.system() == 'Windows':
    lib_name = 'libvertices.dll'

# Define the compile command
compile_command = f"gcc -shared -o {lib_name} -fPIC {c_source_file}"

print(f"Compiling C code with command: {compile_command}")

# Execute the compilation command
exit_code = os.system(compile_command)

# Check if compilation was successful
if exit_code != 0:
    print("\n--- C COMPILATION FAILED ---")
    print("Please ensure you have a C compiler (like GCC) installed and in your system's PATH.")
    sys.exit(1)

print("C library compiled successfully.")

# Load the newly created shared library
try:
    lib = ctypes.CDLL(os.path.abspath(lib_name))
except OSError as e:
    print(f"Error loading library: {e}")
    sys.exit(1)


# --- Part 2: Define the C Function Signature in Python ---

find_vertices_c = lib.findTriangleVertices

find_vertices_c.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

find_vertices_c.restype = ctypes.c_int


# --- Part 3: Call the C function and get vertices ---

A1, B1, C1 = 3.0, -4.0, 6.0
A2, B2, C2 = 3.0, 1.0, -9.0

ax, ay = ctypes.c_double(), ctypes.c_double()
bx, by = ctypes.c_double(), ctypes.c_double()
cx, cy = ctypes.c_double(), ctypes.c_double()

status = find_vertices_c(
    A1, B1, C1, A2, B2, C2,
    ctypes.byref(ax), ctypes.byref(ay),
    ctypes.byref(bx), ctypes.byref(by),
    ctypes.byref(cx), ctypes.byref(cy)
)

if status != 0:
    print("Error: The C function reported that the lines are parallel.")
    sys.exit(1)

a = (ax.value, ay.value)
b = (bx.value, by.value)
c = (cx.value, cy.value)

print("\n--- Vertices calculated from C function ---")
print(f"Vertex A: {a}")
print(f"Vertex B: {b}")
print(f"Vertex C: {c}")


# --- Part 4: Plotting the Graph (Merged Code) ---

x = np.linspace(-4, 6, 400)

y1 = (3 * x + 6) / 4
y2 = -3 * x + 9

plt.figure(figsize=(8, 6))

plt.plot(x, y1, label='3x - 4y + 6 = 0')
plt.plot(x, y2, label='3x + y - 9 = 0')

vertices_x = [a[0], b[0], c[0]]
vertices_y = [a[1], b[1], c[1]]
plt.scatter(vertices_x, vertices_y, color='red', zorder=5)

plt.fill(vertices_x, vertices_y, 'gray', alpha=0.3, label='Triangle Area')

# --- CORRECTED ANNOTATION LOGIC ---
vertices_list = [a, b, c]
labels = ['A', 'B', 'C']

for i, (vx, vy) in enumerate(vertices_list):
    label_text = f'{labels[i]} ({vx:.2f}, {vy:.2f})'
    
    # Adjust alignment based on vertex position
    if labels[i] == 'A': # On x-axis, slightly left and below
        plt.text(vx - 0.1, vy - 0.4, label_text, ha='right', va='top')
    elif labels[i] == 'B': # On x-axis, slightly right and below
        plt.text(vx + 0.1, vy - 0.4, label_text, ha='left', va='top')
    elif labels[i] == 'C': # Above x-axis, slightly right and above
        plt.text(vx + 0.1, vy + 0.2, label_text, ha='left', va='bottom')

# --- END CORRECTED ANNOTATION LOGIC ---

plt.title('Graph of Linear Equations (Vertices from C)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axis('equal')
plt.show()
