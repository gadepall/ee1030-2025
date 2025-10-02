# call.py
import ctypes
import numpy as np

N = 100
xs = np.zeros(N)
ys = np.zeros(N)
zs = np.zeros(N)
normal = np.zeros(3)

lib = ctypes.cdll.LoadLibrary('./line.so')
arrtype = np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS')

lib.line_points.argtypes = [arrtype, arrtype, arrtype, ctypes.c_int]
lib.line_points(xs, ys, zs, N)

lib.normal_vector.argtypes = [arrtype]
lib.normal_vector(normal)

np.savez('points.npz', xs=xs, ys=ys, zs=zs, normal=normal)

