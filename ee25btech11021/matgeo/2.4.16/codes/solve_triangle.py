

import ctypes
import numpy as np

# Load shared object
lib = ctypes.CDLL("./gen_points.so")

# Call C functions
lib.generate_points_isosceles(b"iso_points.dat")
lib.generate_points_right(b"right_points.dat")

# Load points
iso_points = np.loadtxt("iso_points.dat")
right_points = np.loadtxt("right_points.dat")

# Distance squared function
def dist2(P, Q):
    return np.sum((P - Q) ** 2)

# --------- Part (a) Isosceles Triangle -----------
A, B, C = iso_points
AB2 = dist2(A, B)
BC2 = dist2(B, C)
CA2 = dist2(C, A)

print("Isosceles Triangle Check:")
print("AB^2 =", AB2, "BC^2 =", BC2, "CA^2 =", CA2)
isosceles = (AB2 == BC2) or (BC2 == CA2) or (CA2 == AB2)
print("Isosceles:", isosceles)
print()

# --------- Part (b) Right Angled Triangle ---------
P, Q, R = right_points
PQ2 = dist2(P, Q)
QR2 = dist2(Q, R)
RP2 = dist2(R, P)

print("Right Angled Triangle Check:")
print("PQ^2 =", PQ2, "QR^2 =", QR2, "RP^2 =", RP2)
right_angle = (PQ2 + QR2 == RP2) or (QR2 + RP2 == PQ2) or (RP2 + PQ2 == QR2)
print("Right Angled:", right_angle)

