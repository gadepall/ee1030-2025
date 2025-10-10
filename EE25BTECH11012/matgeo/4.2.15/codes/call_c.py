# File: main.py
import ctypes
import platform

# --- 1. Define a Python class that mirrors the C struct ---
class Vector2D(ctypes.Structure):
    fields = [("x", ctypes.c_float),
                ("y", ctypes.c_float)]

# --- 2. Load the shared library ---
if platform.system() == "Windows":
    lib_path = "./libline.dll"
else:
    lib_path = "./libline.so"

try:
    lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading library: {e}")
    print("Have you compiled line_vectors.c?")
    exit()

# --- 3. Define the function signature ---
lib.get_line_vectors.argtypes = [
    ctypes.c_float,            # A
    ctypes.c_float,            # B
    ctypes.POINTER(Vector2D),  # normal_out (output)
    ctypes.POINTER(Vector2D)   # direction_out (output)
]
lib.get_line_vectors.restype = None

# --- 4. Prepare data and call the C function ---
# Hardcoded input values for the line 2x - y = 0
A = 2.0
B = -1.0

# Create empty instances of our Vector2D class for the output
normal_vector = Vector2D()
direction_vector = Vector2D()

# Call the C function with the hardcoded inputs
lib.get_line_vectors(A, B, ctypes.byref(normal_vector), ctypes.byref(direction_vector))

# --- 5. Print the results ---
print("For the line y = 2x (or 2x - y = 0):")
print("----------------------------------------")
print(f"Calculated Normal Vector   (A, B)  : <{normal_vector.x:.1f}, {normal_vector.y:.1f}>")
print(f"Calculated Direction Vector (-B, A): <{direction_vector.x:.1f}, {direction_vector.y:.1f}>")