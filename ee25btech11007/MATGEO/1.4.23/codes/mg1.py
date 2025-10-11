import ctypes
import matplotlib.pyplot as plt

# Load the shared library compiled from mg1.c
lib = ctypes.CDLL("./mg1o.so")

# Define argument and return types for the function inside mg1.c
lib.sectionFormula.argtypes = [
    ctypes.c_float, ctypes.c_float,   # Px, Py
    ctypes.c_float, ctypes.c_float,   # Qx, Qy
    ctypes.c_int, ctypes.c_int,       # m, n
    ctypes.c_int,                     # flag (1=internal, -1=external)
    ctypes.POINTER(ctypes.c_float),   # Rx
    ctypes.POINTER(ctypes.c_float)    # Ry
]
lib.sectionFormula.restype = None

# Example points (P = (3,-2), Q = (1,1)), ratio 2:1
Px, Py = 3.0, -2.0
Qx, Qy = 1.0, 1.0
m, n = 2, 1

# Prepare storage for results
Rx_int, Ry_int = ctypes.c_float(), ctypes.c_float()
Rx_ext, Ry_ext = ctypes.c_float(), ctypes.c_float()

# Call C function (from mg1.c via mg1o.so)
lib.sectionFormula(Px, Py, Qx, Qy, m, n, 1,  ctypes.byref(Rx_int), ctypes.byref(Ry_int))   # internal
lib.sectionFormula(Px, Py, Qx, Qy, m, n, -1, ctypes.byref(Rx_ext), ctypes.byref(Ry_ext))  # external

print("Internal Division:", Rx_int.value, Ry_int.value)
print("External Division:", Rx_ext.value, Ry_ext.value)

# --- Plotting ---
plt.figure(figsize=(6,6))

# Plot P, Q, R_int, R_ext
plt.scatter([Px, Qx, Rx_int.value, Rx_ext.value],
            [Py, Qy, Ry_int.value, Ry_ext.value],
            color=["red","blue","green","purple"], s=100)

plt.text(Px+0.1, Py+0.1, "P", color="red")
plt.text(Qx+0.1, Qy+0.1, "Q", color="blue")
plt.text(Rx_int.value+0.1, Ry_int.value+0.1, "R_int", color="green")
plt.text(Rx_ext.value+0.1, Ry_ext.value+0.1, "R_ext", color="purple")

# Line PQ
plt.plot([Px, Qx], [Py, Qy], "k--")

plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.xlabel("Coefficient of a")
plt.ylabel("Coefficient of b")
plt.title("Section Formula using C (mg1.c) + Python")
plt.grid(True)
plt.show()
