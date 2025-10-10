import ctypes, os, numpy as np, matplotlib.pyplot as plt

# load the shared library (adjust name for macOS: libcircle.dylib, Windows: circle.dll)
lib = ctypes.CDLL(os.path.abspath("./libcircle.so"))

lib.compute_circle.argtypes = [ctypes.c_double, ctypes.c_double,
                               ctypes.c_double, ctypes.c_double,
                               ctypes.POINTER(ctypes.c_double),
                               ctypes.POINTER(ctypes.c_double),
                               ctypes.POINTER(ctypes.c_double)]

def compute_circle(x1, y1, x2, y2):
    cx = ctypes.c_double()
    cy = ctypes.c_double()
    r  = ctypes.c_double()
    lib.compute_circle(x1, y1, x2, y2, ctypes.byref(cx), ctypes.byref(cy), ctypes.byref(r))
    return cx.value, cy.value, r.value

# given endpoints
x1, y1 = -6.0, 3.0
x2, y2 =  6.0, 4.0
cx, cy, r = compute_circle(x1, y1, x2, y2)
print("Center:", (cx, cy), "Radius:", r)

# make a circle for plotting
t = np.linspace(0, 2*np.pi, 400)
xc = cx + r*np.cos(t)
yc = cy + r*np.sin(t)

fig, ax = plt.subplots()
ax.plot(xc, yc, label="Circle")
ax.plot([x1, x2], [y1, y2], 'o-', label="Diameter endpoints")
ax.plot(cx, cy, 'o', label="Center")

ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()
ax.set_title(f"Circle with diameter [({x1},{y1}) ↔ ({x2},{y2})]\nCenter=({cx:.2f},{cy:.2f}), r={r:.4f}")
plt.show()

