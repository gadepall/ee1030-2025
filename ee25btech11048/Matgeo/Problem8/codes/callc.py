import ctypes

# Load the shared C library
lib = ctypes.CDLL("./points.so")

# Specify the return type of the C function
lib.compute_distance.restype = ctypes.c_double

# Call the C function
distance = lib.compute_distance()

# Store the distance in another variable
final_distance = distance

# Print the distance
print("Distance from point (1,-2,9) to intersection point (7,6,9):", final_distance)

# Optional: manual check in Python
A = [1, -2, 9]
P = [7, 6, 9]

# Compute vector difference
v = [P[i] - A[i] for i in range(3)]

# Compute distance manually
manual_distance = (v[0]**2 + v[1]**2 + v[2]**2)**0.5

print("Manual calculation in Python:", manual_distance)

