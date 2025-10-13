import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# --- Load the C library ---
lib_path = os.path.abspath("./reflection.so")
try:
    c_lib = ctypes.CDLL(lib_path)
except OSError:
    print("❌ reflection.so not found. Compile with: gcc -shared -o reflection.so -fPIC reflection.c")
    exit()

# Define function signature
c_lib.reflect_ray.argtypes = [ctypes.c_float, ctypes.c_float,
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float)]

# --- Incident ray direction (line x+3y=3 has direction (-3,1)) ---
dx, dy = -3.0, 1.0
rx, ry = ctypes.c_float(), ctypes.c_float()

# Call C function
c_lib.reflect_ray(ctypes.c_float(dx), ctypes.c_float(dy),
                  ctypes.byref(rx), ctypes.byref(ry))

print(f"Incident direction = ({dx}, {dy})")
print(f"Reflected direction = ({rx.value}, {ry.value})")

# --- Geometry ---
# Point of incidence (intersection with x-axis)
P = (3, 0)

# Parametric plotting
t = np.linspace(-1, 2, 100)
incident_x = P[0] + dx * t
incident_y = P[1] + dy * t

reflected_x = P[0] + rx.value * t
reflected_y = P[1] + ry.value * t

# --- Plot ---
plt.figure(figsize=(6,6))
plt.plot(incident_x, incident_y, "b", label="Incident Ray")
plt.plot(reflected_x, reflected_y, "r", label="Reflected Ray")

# Mark incidence point
plt.scatter(*P, color="black", s=60, zorder=5)
plt.text(P[0]+0.1, P[1]+0.2, "P(3,0)", fontsize=10)

# Axes formatting
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.gca().set_aspect("equal")
plt.xlim(-2, 6)
plt.ylim(-3, 3)

plt.title("Reflection of Ray $x+3y=3$ at the X-axis (via C function)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
