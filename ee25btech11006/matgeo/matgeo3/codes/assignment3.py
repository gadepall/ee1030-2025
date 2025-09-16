import numpy as np
import ctypes

# Load C library
c_lib = ctypes.CDLL('./3c_q2_3_9.so')

c_lib.dotfinder.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float,
                            ctypes.c_float, ctypes.c_float, ctypes.c_float]
c_lib.dotfinder.restype = ctypes.c_float

# Given magnitudes
a_mag = 1/2
b_mag = 4/np.sqrt(3)
cross_mag = 1/np.sqrt(3)

# Find angle θ using |a×b| = |a||b|sinθ
sin_theta = cross_mag / (a_mag * b_mag)
theta1 = np.degrees(np.arcsin(sin_theta))
theta2 = 180 - theta1

print("Possible angles:", theta1, "or", theta2)

# Compute a·b using cosθ
dot1 = c_lib.dotfinder(a_mag,0,0, b_mag*np.cos(np.radians(theta1)), b_mag*np.sin(np.radians(theta1)),0)
dot2 = c_lib.dotfinder(a_mag,0,0, b_mag*np.cos(np.radians(theta2)), b_mag*np.sin(np.radians(theta2)),0)

print("Possible values of a·b:", dot1, "or", dot2)