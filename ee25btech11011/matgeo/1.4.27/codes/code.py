import ctypes
import os

# Load the shared library
if os.name == "nt":  # Windows
    lib = ctypes.CDLL("./externaldivision.dll")
else:
    lib = ctypes.CDLL("./libexternaldivision.so")

# Define argument and return types for safety
lib.external_division.argtypes = [
    ctypes.c_float, ctypes.c_float,
    ctypes.c_float, ctypes.c_float,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)
]
lib.external_division.restype = None

def external_division(ax, ay, bx, by, k=3):
    cx = ctypes.c_float()
    cy = ctypes.c_float()
    lib.external_division(ax, ay, bx, by, k, ctypes.byref(cx), ctypes.byref(cy))
    return cx.value, cy.value


if __name__ == "__main__":
    ax, ay = map(float, input("Enter coordinates of A (ax ay): ").split())
    bx, by = map(float, input("Enter coordinates of B (bx by): ").split())
    k = int(input("Enter ratio k (default 3): ") or 3)

    cx, cy = external_division(ax, ay, bx, by, k)
    print(f"C divides AB externally in ratio {k}:1 at ({cx:.2f}, {cy:.2f})")
