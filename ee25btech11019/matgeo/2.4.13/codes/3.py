import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared C library
lib = ctypes.CDLL('./3.so')
lib.compute_points.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                               ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                               ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.compute_points.restype = None

# Prepare variables
Px = ctypes.c_double()
Py = ctypes.c_double()
Pz = ctypes.c_double()
Qx = ctypes.c_double()
Qy = ctypes.c_double()
Qz = ctypes.c_double()

# Call C function
lib.compute_points(ctypes.byref(Px), ctypes.byref(Py), ctypes.byref(Pz),
                   ctypes.byref(Qx), ctypes.byref(Qy), ctypes.byref(Qz))

# Extract results
P = np.array([Px.value, Py.value, Pz.value])
Q = np.array([Qx.value, Qy.value, Qz.value])
print(f"P = {P}, Q = {Q}")

# Given data
A = np.array([6, 7, 4])
AB = np.array([3, -1, 1])
C = np.array([0, -9, 2])
CD = np.array([-3, 2, 4])

# Generate line AB and CD
t = np.linspace(-5, 5, 100)
lineAB = A.reshape(3,1) + np.outer(AB, t)
lineCD = C.reshape(3,1) + np.outer(CD, t)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(lineAB[0], lineAB[1], lineAB[2], label="Line AB")
ax.plot(lineCD[0], lineCD[1], lineCD[2], label="Line CD")

# Points
ax.scatter(A[0], A[1], A[2], color='red', label='A')
ax.scatter(C[0], C[1], C[2], color='blue', label='C')
ax.scatter(P[0], P[1], P[2], color='green', label='P')
ax.scatter(Q[0], Q[1], Q[2], color='purple', label='Q')

# Connect PQ
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], 'k--', label="PQ ⟂ AB,CD")

ax.legend()
plt.savefig("3.png")
plt.show()
