import ctypes

lib = ctypes.CDLL('./libverify.so')

lib.verify_circle.argtypes = [
    ctypes.c_float, ctypes.c_float,
    ctypes.c_float, ctypes.c_float,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float)
]
lib.verify_circle.restype = None

px, py = ctypes.c_float(-2.0), ctypes.c_float(4.0)
cx, cy = ctypes.c_float(3.0), ctypes.c_float(5.0)
radius = ctypes.c_float(6.0)
result = ctypes.c_float()

lib.verify_circle(px, py, cx, cy, radius, ctypes.byref(result))

if result.value == 1.0:
    print("Verified: Point lies on the circle")
else:
    print("Verified: Point does NOT lie on the circle")
