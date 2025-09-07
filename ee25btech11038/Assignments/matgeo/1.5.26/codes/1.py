import ctypes

# Load the shared library
import os 
lib_path= os.path.abspath('1.so')
lib=ctypes.CDLL(lib_path)

# Define argument and return types for the function
# void trisect_points(double ax, double ay, double bx, double by, double *px, double *py, double *qx, double *qy)

lib.trisect_points.argtypes = [
            ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
                    ]
lib.trisect_points.restype = None

# Variables to hold the result
px = ctypes.c_double()
py = ctypes.c_double()
qx = ctypes.c_double()
qy = ctypes.c_double()

# Inputs (A = (2,-2), B = (-7,4))
ax, ay, bx, by = 2, -2, -7, 4

# Call the C function
lib.trisect_points(ax, ay, bx, by,
                           ctypes.byref(px), ctypes.byref(py),
                                              ctypes.byref(qx), ctypes.byref(qy))

print(f"Trisection Point P (nearer to A): ({px.value}, {py.value})")
print(f"Trisection Point Q (nearer to B): ({qx.value}, {qy.value})")
