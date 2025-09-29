import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the compiled C library
lib = ctypes.CDLL("./findA.so")

# Define the function signature: void findA(int, int, int, int, int*, int*)
lib.findA.argtypes = [
    ctypes.c_int, ctypes.c_int,
    ctypes.c_int, ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int)
]
lib.findA.restype = None  # void

def findA(xp, yp, xb, yb):
    """Call the C function via ctypes."""
    xa = ctypes.c_int()
    ya = ctypes.c_int()
    lib.findA(xp, yp, xb, yb, ctypes.byref(xa), ctypes.byref(ya))
    return xa.value, ya.value
    
if __name__ == "__main__":
    xp, yp = 3, 4
    xb, yb = 1, 2

    xa, ya = findA(xp, yp, xb, yb)
    print(f"Coordinates of A (from C): ({xa}, {ya})")

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.plot(xp, yp, 'ro', label='P')
    plt.plot(xb, yb, 'bo', label='B')
    plt.plot(xa, ya, 'go', label='A')
    plt.plot([xb, xa], [yb, ya], 'k--', label='Line BA')

    plt.text(xp+0.1, yp+0.1, "P")
    plt.text(xb+0.1, yb+0.1, "B")
    plt.text(xa+0.1, ya+0.1, "A")

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.title("Reflection of B across P (computed by C, plotted by Python)")
    plt.show()

