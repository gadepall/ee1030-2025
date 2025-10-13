import ctypes
# Load the shared object
lib = ctypes.CDLL("./curves.so")

# Specify return type
lib.compute_points_and_area.restype = ctypes.POINTER(ctypes.c_double)

# Call the function
result_ptr = lib.compute_points_and_area()
results = [result_ptr[i] for i in range(5)]

P1 = (results[0], results[1])
P2 = (results[2], results[3])
area = results[4]

print("Intersection points:")
print("P1:", P1)
print("P2:", P2)
print("Area bounded by curves:", area)
