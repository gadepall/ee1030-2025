import ctypes
import numpy as np
import matplotlib.pyplot as plt
import os

lib_file = "mat.so"
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lib_file)

c_library = ctypes.CDLL(lib_path)

# --- Step 2: Define the function's signature ---
lib_function = c_library.calculate_tangent_points
lib_function.argtypes = [
    ctypes.c_double,
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
lib_function.restype = None

# --- Step 3: Prepare arguments and call the C function ---
radius = 5.0
angle_deg = 60.0

h_coords = np.zeros(2, dtype=np.double)
poc1_coords = np.zeros(2, dtype=np.double)
poc2_coords = np.zeros(2, dtype=np.double)

h_ptr = h_coords.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
poc1_ptr = poc1_coords.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
poc2_ptr = poc2_coords.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call the C function
lib_function(radius, angle_deg, h_ptr, poc1_ptr, poc2_ptr)

print("\nCoordinates returned from C function:")
print(f"Tangent Intersection (h): ({h_coords[0]:.2f}, {h_coords[1]:.2f})")
print(f"Point of Contact 1 (poc1): ({poc1_coords[0]:.2f}, {poc1_coords[1]:.2f})")
print(f"Point of Contact 2 (poc2): ({poc2_coords[0]:.2f}, {poc2_coords[1]:.2f})")

# --- Step 4: Plot the results ---
fig, ax = plt.subplots(figsize=(12, 10))

circle = plt.Circle((0, 0), radius, color='skyblue', fill=False, lw=2, label=f'Circle (r={radius})')
ax.add_patch(circle)

ax.plot([h_coords[0], poc1_coords[0]], [h_coords[1], poc1_coords[1]], 'g-', label='Tangent 1')
ax.plot([h_coords[0], poc2_coords[0]], [h_coords[1], poc2_coords[1]], 'g-')

ax.plot(h_coords[0], h_coords[1], 'ro', markersize=8, label='Intersection h')
ax.plot(poc1_coords[0], poc1_coords[1], 'mo', markersize=8, label='Points of Contact')
ax.plot(poc2_coords[0], poc2_coords[1], 'mo')
ax.plot(0, 0, 'ko', markersize=8, label='Center O')

ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':')
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.set_title(f'Tangents to a Circle Inclined at {angle_deg}°', fontsize=16)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.legend()

plt.savefig('1.png')
plt.show()