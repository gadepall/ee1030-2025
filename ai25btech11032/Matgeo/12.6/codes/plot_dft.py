import ctypes
import numpy as np
import matplotlib.pyplot as plt
from numpy.ctypeslib import ndpointer

# Load the C library
lib = ctypes.CDLL("./libdft.so")

# Define function signature
lib.dft.argtypes = [
    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),  # input x
    ctypes.c_int,                                      # N
    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),  # output Xr
    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),  # output Xi
]
lib.dft.restype = None

# Input signal
x = np.array([1.0, 0.0, 2.0, 3.0], dtype=np.float64)
N = len(x)

# Allocate outputs
Xr = np.zeros(N, dtype=np.float64)
Xi = np.zeros(N, dtype=np.float64)

# Call C function
lib.dft(x, N, Xr, Xi)

# Convert to magnitude and phase
X = Xr + 1j*Xi
mag = np.abs(X)
phase = np.angle(X)

# --- Plot ---
k = np.arange(N)

plt.figure()
plt.stem(k, mag, basefmt=" ")
plt.title("Magnitude Spectrum |X[k]|")
plt.xlabel("k")
plt.ylabel("|X[k]|")
plt.savefig("fig1.png")
plt.show()

plt.figure()
plt.stem(k, phase, basefmt=" ")
plt.title("Phase Spectrum ∠X[k]")
plt.xlabel("k")
plt.ylabel("Phase [rad]")
plt.savefig("fig2.png")
plt.show()

