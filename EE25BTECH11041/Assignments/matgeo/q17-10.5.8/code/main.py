# main.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from math import acos, sqrt

# Load the shared object file (compiled C code)
lib = ctypes.CDLL("./main.so")

# Define argument and return types for the C function
lib.tangent_length.argtypes = [ctypes.c_double, ctypes.c_double]
lib.tangent_length.restype = ctypes.c_double

# Given radii
r = 3.0
R = 5.0

# Call C function to get tangent length
tangent_len_c = lib.tangent_length(R, r)

if tangent_len_c < 0:
    raise ValueError("Invalid radii: R must be greater than r")

print(f"[C Function] Tangent length (√(R²−r²)) = {tangent_len_c:.3f} cm")

# Now use geometry to verify and plot
theta = np.deg2rad(60)
O = np.array([0.0, 0.0])
P = np.array([R * np.cos(theta), R * np.sin(theta)])

# Compute tangent points
beta = acos(r / R)
T1 = np.array([r * np.cos(theta + beta), r * np.sin(theta + beta)])
T2 = np.array([r * np.cos(theta - beta), r * np.sin(theta - beta)])

# Verify length geometrically
L1 = np.linalg.norm(P - T1)
L2 = np.linalg.norm(P - T2)

print(f"[Python Geometry] PT1 = {L1:.3f} cm, PT2 = {L2:.3f} cm")

# Plot
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal', 'box')
ax.set_title("Tangents from a Point on Outer Circle to Inner Circle")

# Circles
outer = plt.Circle((0,0), R, fill=False, color='blue', linestyle='--', label='Outer Circle (R=5 cm)')
inner = plt.Circle((0,0), r, fill=False, color='green', linestyle='--', label='Inner Circle (r=3 cm)')
ax.add_patch(outer)
ax.add_patch(inner)

# Lines
ax.plot([0, P[0]], [0, P[1]], 'k-', label='OP')
ax.plot([P[0], T1[0]], [P[1], T1[1]], 'r-', label='Tangent 1')
ax.plot([P[0], T2[0]], [P[1], T2[1]], 'r-')
ax.plot([0, T1[0]], [0, T1[1]], 'gray', linestyle=':')
ax.plot([0, T2[0]], [0, T2[1]], 'gray', linestyle=':')

# Points
ax.plot(0, 0, 'ko')
ax.plot(P[0], P[1], 'ro')
ax.plot(T1[0], T1[1], 'go')
ax.plot(T2[0], T2[1], 'go')

ax.text(0.2, -0.3, 'O', fontsize=10)
ax.text(P[0]*1.05, P[1]*1.05, 'P', fontsize=10)
ax.text(T1[0]*1.05, T1[1]*1.05, 'T1', fontsize=10)
ax.text(T2[0]*1.05, T2[1]*1.05, 'T2', fontsize=10)

ax.legend()
ax.grid(True)
plt.show()

