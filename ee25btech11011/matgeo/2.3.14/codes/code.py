import ctypes
import math
import os

# Load the compiled shared library
if os.name == "nt":
    lib = ctypes.CDLL("./direction.dll")  # Windows
else:
    lib = ctypes.CDLL("./direction.so")   # Linux/macOS

# Define Vector3 struct in Python
class Vector3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Tell Python about the C functions signatures
lib.fromDirectionCosines.argtypes = [ctypes.c_double, ctypes.c_double]
lib.fromDirectionCosines.restype = Vector3

lib.dotProduct.argtypes = [Vector3, Vector3]
lib.dotProduct.restype = ctypes.c_double

# Call C function to get unit direction vector
angle_x = 30.0
angle_y = 120.0
direction = lib.fromDirectionCosines(angle_x, angle_y)

print("Unit direction vector (from C):")
print(f"x = {direction.x:.6f}")
print(f"y = {direction.y:.6f}")
print(f"z = {direction.z:.6f}")

# Compute angle with z-axis using dot product from C
e_z = Vector3(0.0, 0.0, 1.0)
cos_gamma = lib.dotProduct(direction, e_z)
gamma_deg = math.degrees(math.acos(cos_gamma))

print(f"Angle with z-axis = {gamma_deg:.2f} degrees")
