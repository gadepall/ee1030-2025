import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./code.so')

# Define argument and return types
lib.solve_car_speeds.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

# Function to call C function
def get_speeds(distance, time_same_dir, time_towards):
    v1 = ctypes.c_double()
    v2 = ctypes.c_double()
    lib.solve_car_speeds(distance, time_same_dir, time_towards, ctypes.byref(v1), ctypes.byref(v2))
    return v1.value, v2.value

# Example
distance = 100.0
time_same_dir = 5.0
time_towards = 1.0

v1, v2 = get_speeds(distance, time_same_dir, time_towards)
print(f"v1 = {v1}, v2 = {v2}")

# Plot the lines v1 + v2 = distance / time_towards and v1 - v2 = distance / time_same_dir
v2_vals = np.linspace(0, 100, 200)
v1_towards = distance / time_towards - v2_vals
v1_same = distance / time_same_dir + v2_vals

plt.plot(v2_vals, v1_towards, color='blue')
plt.plot(v2_vals, v1_same, color='red')
plt.plot(v2, v1, 'ko')  # intersection
plt.xlabel('v2 (km/h)')
plt.ylabel('v1 (km/h)')
plt.grid(True)
plt.savefig("/home/arsh-dhoke/ee1030-2025/ee25btech11010/matgeo/5.8.8/figs/speed.png")
plt.show()
