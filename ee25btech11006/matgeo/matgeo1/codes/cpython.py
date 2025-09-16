import ctypes

lib = ctypes.CDLL('./mat1.so')

lib.sectionFormula.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_float,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float)
]
lib.sectionFormula.restype = None

lib.sectionFormulaExternal.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_float,
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float)
]
lib.sectionFormulaExternal.restype = None

p1 = (ctypes.c_float * 3)(1.0, -2.0, 3.0)
p2 = (ctypes.c_float * 3)(3.0, 4.0, -5.0)
res_internal = (ctypes.c_float * 3)()
res_external = (ctypes.c_float * 3)()
m = 2.0
n = 3.0

lib.sectionFormula(p1, p2, m, n, res_internal)
lib.sectionFormulaExternal(p1, p2, m, n, res_external)

print("Internal division (2:3): [{:.2f}, {:.2f}, {:.2f}]".format(
    res_internal[0], res_internal[1], res_internal[2]
))
print("External division (2:3): [{:.2f}, {:.2f}, {:.2f}]".format(
    res_external[0], res_external[1], res_external[2]
))