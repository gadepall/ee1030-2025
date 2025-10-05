import ctypes
import numpy as np

lib = ctypes.CDLL('./libregression.so')

get_data = lib.get_data
get_data.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int)
]
get_data.restype = None

years = np.zeros(6, dtype=np.double)
prod = np.zeros(6, dtype=np.double)
n = ctypes.c_int()
get_data(
    years.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    prod.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    ctypes.byref(n)
)

print('Years:', years[:n.value])
print('Production:', prod[:n.value])

get_stats = lib.get_stats
stats = np.zeros(3, dtype=np.double)
get_stats(
    years.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    prod.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    n,
    stats.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)
print('Alpha:', stats[0])
print('Beta:', stats[1])
print('Alpha + Beta:', stats[2])

