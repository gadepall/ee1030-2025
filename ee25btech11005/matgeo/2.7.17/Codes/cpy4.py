import ctypes
import numpy as np

lib = ctypes.CDLL('./mat4.so')

lib.vector_subtract.argtypes = (np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'))
lib.vector_subtract.restype = None

lib.dot_product.argtypes = (np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                           np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'))
lib.dot_product.restype = ctypes.c_double

lib.cross_product.argtypes = (np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                             np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                             np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'))
lib.cross_product.restype = None

lib.magnitude.argtypes = (np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),)
lib.magnitude.restype = ctypes.c_double

lib.is_right_angle.argtypes = (np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                              np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'))
lib.is_right_angle.restype = ctypes.c_int

lib.triangle_area.argtypes = (np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                             np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'))
lib.triangle_area.restype = ctypes.c_double

lib.which_right_angle.argtypes = (np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                 np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
                                 np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'))
lib.which_right_angle.restype = ctypes.c_int


def vector_subtract(u, v):
    res = np.zeros(3, dtype=np.double)
    lib.vector_subtract(res, np.ascontiguousarray(u, dtype=np.double),
                       np.ascontiguousarray(v, dtype=np.double))
    return res


def is_right_angle(u, v):
    return lib.is_right_angle(np.ascontiguousarray(u, dtype=np.double),
                             np.ascontiguousarray(v, dtype=np.double)) == 1


def triangle_area(u, v):
    return lib.triangle_area(np.ascontiguousarray(u, dtype=np.double),
                            np.ascontiguousarray(v, dtype=np.double))


def which_right_angle(A, B, C):
    return lib.which_right_angle(np.ascontiguousarray(A, dtype=np.double),
                                 np.ascontiguousarray(B, dtype=np.double),
                                 np.ascontiguousarray(C, dtype=np.double))


A = np.array([2, -1, 1], dtype=np.double)
B = np.array([1, -3, -5], dtype=np.double)
C = np.array([3, -4, -4], dtype=np.double)

vertex = which_right_angle(A, B, C)
if vertex == 0:
    print("Triangle is not right-angled at any vertex.")
elif vertex == 1:
    print("Triangle is right-angled at A.")
elif vertex == 2:
    print("Triangle is right-angled at B.")
elif vertex == 3:
    print("Triangle is right-angled at C.")

AB = vector_subtract(B, A)
AC = vector_subtract(C, A)
area = triangle_area(AB, AC)

print("Area of the triangle: ", area)

