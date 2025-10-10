import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./magnitude.so')

# Specify argument and return types for the C function
lib.get_x_coords.argtypes = [
    ctypes.c_float, # ax
    ctypes.c_float, # ay
    ctypes.POINTER(ctypes.c_float), # x_out
    ctypes.POINTER(ctypes.c_float)  # y_out
]
lib.get_x_coords.restype = None

# Define the unit vector a direction
ax, ay = 1.0, 0.0 # (Choose your direction; this is along x-axis)

x_out = ctypes.c_float()
y_out = ctypes.c_float()

# Call the C function
lib.get_x_coords(ax, ay, ctypes.byref(x_out), ctypes.byref(y_out))

# Prepare points for plotting
origin = np.array([0, 0])
a = np.array([ax, ay]) # Unit vector
x = np.array([x_out.value, y_out.value]) # Solution from C

plt.figure(figsize=(6, 6))

# Draw vector a
plt.quiver(origin[0], origin[1], a[0], a[1], angles='xy', scale_units='xy', scale=1, color='green', label='a (unit)')
plt.text(a[0], a[1], f'a({a[0]:.1f}, {a[1]:.1f})', fontsize=10, ha='left', va='bottom')

# Draw vector x
plt.quiver(origin[0], origin[1], x[0], x[1], angles='xy', scale_units='xy', scale=1, color='blue', label='x = 3a')
plt.text(x[0], x[1], f'x({x[0]:.1f}, {x[1]:.1f})', fontsize=10, ha='left', va='bottom')

# Draw origin
plt.scatter(origin[0], origin[1], color='black', s=40)
plt.text(origin[0], origin[1], 'O(0,0)', fontsize=10, ha='left', va='top')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Figure")
plt.legend()
plt.grid(True)
plt.xlim(-1, 4)
plt.ylim(-1, 2)
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/2.8.8/figs/figure1.png")
plt.show()
