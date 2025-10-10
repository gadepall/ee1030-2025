import ctypes
import numpy

lib = ctypes.CDLL("./computations.so")

lib.find_angle.argtypes = [
    ctypes.POINTER((ctypes.c_int * 3)),
    ctypes.POINTER((ctypes.c_int * 3))
]
lib.find_angle.restype = ctypes.c_double

def compute_angle(u, v):
    u_arr = (ctypes.c_int * 3)(*u)
    v_arr = (ctypes.c_int * 3)(*v)
    theta = lib.find_angle(u_arr, v_arr)
    return theta

u = [1, -2, -2]
v = [3, -6, 2]
theta = compute_angle(u, v)

print(f"Angle (radians): {theta}")
print(f"Angle (degrees): {theta * 180 / numpy.pi}")
