import ctypes
import platform

# --- 1. Define a Python class that mirrors the C struct ---
# The names and types in fields must exactly match the C struct.
class Vector(ctypes.Structure):
    fields = [("coeff_a", ctypes.c_int),
                ("coeff_b", ctypes.c_int)]

# --- 2. Load the shared library ---
if platform.system() == "Windows":
    lib_path = "./libvector.dll"
else:
    lib_path = "./libvector.so"

try:
    lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading library: {e}")
    print("Have you compiled vector_ops.c?")
    exit()


# --- 3. Define the function signature (argtypes and restype) ---
# This ensures Python sends the correct data types to the C function.
lib.external_division.argtypes = [
    ctypes.POINTER(Vector), # const Vector* P
    ctypes.POINTER(Vector), # const Vector* Q
    ctypes.c_int,           # int m
    ctypes.c_int,           # int n
    ctypes.POINTER(Vector)  # Vector* R (output)
]
lib.external_division.restype = None # for void return type


# --- 4. Prepare Input and Output Data ---
# Create instances of our Vector class for the inputs
P = Vector(coeff_a=2, coeff_b=1)
Q = Vector(coeff_a=1, coeff_b=-3)

# Define the ratio m:n
m = 1
n = 2

# Create an empty Vector instance to hold the result from the C function.
# This acts as the output buffer.
R = Vector()


# --- 5. Call the C function ---
# The C function will write its result directly into our 'R' object.
lib.external_division(ctypes.byref(P), ctypes.byref(Q), m, n, ctypes.byref(R))


# --- 6. Print the Result ---
# Access the values that the C function wrote into our R object.
print(f"Vector P = ({P.coeff_a})a + ({P.coeff_b})b")
print(f"Vector Q = ({Q.coeff_a})a + ({Q.coeff_b})b")
print(f"Ratio m:n = {m}:{n}")
print("-" * 30)
print(f"The position vector of point R is ({R.coeff_a})a + ({R.coeff_b})b")