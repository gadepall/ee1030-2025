\begin{lstlisting}[language=Python]
import numpy as np
import ctypes
lib = ctypes.CDLL('./vector_calcs.so')
lib.angle_deg.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.angle_deg.restype = ctypes.c_double
A = np.array([1., 1., 1.])
B = np.array([2., 5., 0.])
C = np.array([3., 2., -3.])
D = np.array([1., -6., -1.])
AB = B - A
CD = D - C
AB_c = np.ascontiguousarray(AB, dtype=np.double).ctypes.data_as(ctypes.POINTER(ctypes.c_double))
CD_c = np.ascontiguousarray(CD, dtype=np.double).ctypes.data_as(ctypes.POINTER(ctypes.c_double))
angle = lib.angle_deg(AB_c, CD_c)
print("Angle between AB and CD (degrees):", angle)
lib.collinear.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.collinear.restype = ctypes.c_int
is_collinear = lib.collinear(AB_c, CD_c)
print("Are AB and CD collinear?", "Yes" if is_collinear else "No")
