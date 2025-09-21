import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C shared library
lib = ctypes.CDLL("./libconics.so")

# Define return type
lib.solve_conics.argtypes = [ctypes.POINTER(ctypes.c_double)]

# Prepare results array
results = (ctypes.c_double * 4)()
lib.solve_conics(results)

# Convert to Python list
vals = list(results)
points = [(vals[i], vals[i+1]) for i in range(0, len(vals), 2) if not np.isnan(vals[i])]
print("Solutions :", points)

# ---- Plotting ----

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Intersection of Hyperbola and Parabola")
ax.grid(True)

# Hyperbola: x^2 - y^2 = 180 -> y = ±sqrt(x^2 - 180)
xh = np.linspace(-40, 40, 800)
for sign in [1, -1]:
    yh = sign*np.sqrt(np.maximum(xh**2 - 180, 0))
    ax.plot(xh, yh, 'r', label="Hyperbola" if sign==1 else "")

# Parabola: y^2 = 8x -> y = ±sqrt(8x)
xp = np.linspace(0, 40, 400)
for sign in [1, -1]:
    yp = sign*np.sqrt(8*xp)
    ax.plot(xp, yp, 'b', label="Parabola" if sign==1 else "")

# Intersection points from C
for (px, py) in points:
    ax.plot(px, py, 'ko', markersize=8)
    ax.text(px+0.5, py+0.5, f"({px:.0f},{py:.0f})")

ax.legend()
plt.savefig("/home/user/Matrix Theory: workspace/Matgeo_assignments/9.4.39/figs/Figure_1.png")
plt.show()

