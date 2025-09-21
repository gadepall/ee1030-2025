import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C library
handc = ctypes.CDLL("./func.so")
handc.angle_between.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # u
    ctypes.POINTER(ctypes.c_double)   # v
]
handc.angle_between.restype = ctypes.c_double

def np_to_c(arr):
    return arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Direction vector of line
v = np.array([1.0, -1.0, 0.0], dtype=np.float64)
# Positive Y-axis unit vector
e2 = np.array([0.0, 1.0, 0.0], dtype=np.float64)

theta = handc.angle_between(np_to_c(v), np_to_c(e2))
theta_deg = np.degrees(theta)
print(f"Angle with Y-axis = {theta_deg:.2f} degrees")

# Plot line and Y axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# line through origin in direction v
t = np.linspace(-2, 2, 10)
x_line, y_line, z_line = t*v[0], t*v[1], t*v[2]
ax.plot(x_line, y_line, z_line, label='Line direction (1,-1,0)')

# Y-axis
ax.plot([0,0], [0,2], [0,0], 'g', label='Positive Y-axis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title(f"Angle ≈ {theta_deg:.1f}°")
plt.title("Line vs Y-axis (Python + C)")
plt.savefig("../figs/line_c.png")
plt.show()

