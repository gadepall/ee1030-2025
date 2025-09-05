import ctypes

# Load shared object
collinear = ctypes.CDLL("./collinear.so")

# Configure relation() function
collinear.relation.argtypes = [ctypes.c_int, ctypes.c_int]
collinear.relation.restype = ctypes.c_int

# Example usage
x, y = 1, 2
val = collinear.relation(x, y)

print(f"For point ({x},{y}), relation value = {val}")
print("Equation of line: x + 3y - 7 = 0")

