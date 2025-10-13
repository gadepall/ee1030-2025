import ctypes as ct
import math

lib = ct.CDLL("./problem.so")

class Vector(ct.Structure):
    _fields_ = [("x", ct.c_double), ("y", ct.c_double), ("z", ct.c_double)]

lib.check_conditions.argtypes = [Vector, Vector, Vector, ct.POINTER(ct.c_double)]
lib.check_conditions.restype = None
points = ct.c_double*9
lib.out_data.argtypes = [ct.POINTER(ct.c_double)]
data = points()
lib.out_data(data)

a = Vector(data[0], data[1], data[2])
b = Vector(data[3], data[4], data[5])
c = Vector(data[6], data[7], data[8])

results = (ct.c_double * 4)()
lib.check_conditions(a, b, c, results)

options = ['a', 'b', 'c', 'd']
for i, res in enumerate(results):
    print(f"Option {options[i]}: {'True' if res else 'False'}")
def send_data():
    return data[0], data[1], data[3], data[4], data[6], data[7]
