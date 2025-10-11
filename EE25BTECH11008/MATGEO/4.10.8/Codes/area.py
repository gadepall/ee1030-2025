import ctypes

lib = ctypes.CDLL("./area.so")

lib.triangle_area.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.triangle_area.restype = ctypes.c_double

m1 = float(input("Enter m1: "))
c1 = float(input("Enter c1: "))
m2 = float(input("Enter m2: "))
c2 = float(input("Enter c2: "))

area = lib.triangle_area(m1, c1, m2, c2)
print(f"Triangle area = {area}")
