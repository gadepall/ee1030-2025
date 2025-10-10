import ctypes
import platform

# --- 1. Load the shared library ---
if platform.system() == "Windows":
    lib_path = "./libdistance.dll"
else:
    lib_path = "./libdistance.so"

try:
    lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Error loading library: {e}")
    print("Have you compiled distance_calc.c?")
    exit()

# --- 2. Define the function signature ---
# Set the argument types
lib.calculate_distance.argtypes = [ctypes.c_double, ctypes.c_double]

# IMPORTANT: Set the return type.
# This tells ctypes that the C function returns a double value.
lib.calculate_distance.restype = ctypes.c_double

# --- 3. Get input from the user in Python ---
try:
    m_val = float(input("Enter the value of m: "))
    n_val = float(input("Enter the value of n: "))
except ValueError:
    print("Invalid input. Please enter numbers.")
    exit()

# --- 4. Call the C function and get the returned value ---
distance = lib.calculate_distance(m_val, n_val)

# --- 5. Print the result ---
print("\n--- Calculation performed by C ---")
print(f"Distance between the points ({m_val:.2f}, {-n_val:.2f}) and ({-m_val:.2f}, {n_val:.2f}) is: {distance:.4f}")