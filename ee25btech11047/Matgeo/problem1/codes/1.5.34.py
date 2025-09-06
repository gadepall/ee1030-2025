import ctypes
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./libsection.so")

# Define argument types
lib.section_point.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double,
                              ctypes.c_int, ctypes.c_int,
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]

# Inputs
ax, ay = 2.0, -5.0
bx, by = 5.0, 2.0
m, n = 2, 3

# Outputs
px = ctypes.c_double()
py = ctypes.c_double()

# Call function
lib.section_point(ax, ay, bx, by, m, n, ctypes.byref(px), ctypes.byref(py))

print(f"P = ({px.value}, {py.value})")

# --- Plotting ---
plt.figure(figsize=(5,5))
plt.plot([ax, bx], [ay, by], 'k--', label="Line AB")  # line AB
plt.scatter([ax, bx], [ay, by], color='blue', label="A & B")
plt.scatter(px.value, py.value, color='red', label="P (2:3)")

plt.text(ax, ay, "A(2,-5)", ha='right')
plt.text(bx, by, "B(5,2)", ha='left')
plt.text(px.value, py.value, "P(3.2,-2.2)", ha='left')

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.legend()
plt.grid(True)
plt.show()
