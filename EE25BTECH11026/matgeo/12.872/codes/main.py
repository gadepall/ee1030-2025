import ctypes

lib = ctypes.CDLL('./libsolver.so')

lib.check_solvability.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.check_solvability.restype = ctypes.c_int

b1 = float(input("Enter b1: "))
b2 = float(input("Enter b2: "))
b3 = float(input("Enter b3: "))

# Call the C function
result = lib.check_solvability(b1, b2, b3)

# Print result
if result == 1:
    print(f"Condition satisfied: 3*{b1}+{b2}+2*{b3}=0")
else:
    print(f"Condition NOT satisfied: 3*{b1}+{b2}+2*{b3}≠0")

