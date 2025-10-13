import ctypes

# Load the shared object file
lib = ctypes.CDLL("./sumit_age.so")

# Define return types for functions
lib.son_age.restype = ctypes.c_int
lib.sumit_age.restype = ctypes.c_int

# Call functions from C
son = lib.son_age()
sumit = lib.sumit_age()

# Print results
print("Son's present age =", son, "years")
print("Sumit's present age =", sumit, "years")

