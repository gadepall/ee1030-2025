import ctypes
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libequidistant.so")
lib.compute_point.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

Ax, Ay = -2., 0.
Bx, By = 6., 0
Px, Py = ctypes.c_double(), ctypes.c_double()

lib.compute_point(Ax, Ay, Bx, By, ctypes.byref(Px), ctypes.byref(Py))

Px_val, Py_val = Px.value, Py.value

print(f"A = ({Ax}, {Ay})")
print(f"B = ({Bx}, {By})")
print(f"Computed P = ({Px_val}, {Py_val})")

plt.figure()
plt.scatter([Ax, Bx, Px_val], [Ay, By, Py_val],
            color=["green", "red", "blue"], s=100)

plt.text(Ax + 0.2, Ay, f"A({Ax:.2f},{Ay:.2f})", fontsize=12, color="green")
plt.text(Bx + 0.2, By, f"B({Bx:.2f},{By:.2f})", fontsize=12, color="red")
plt.text(Px_val + 0.2, Py_val, f"P({Px_val:.2f},{Py_val:.2f})", fontsize=12, color="blue")

plt.plot([Ax, Px_val, Bx], [Ay, Py_val, By],
         linestyle="--", color="gray")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Computed P = (A + B)/2")
plt.grid(True)
plt.axis("equal")
plt.savefig("fig2.1.png") 
plt.show()