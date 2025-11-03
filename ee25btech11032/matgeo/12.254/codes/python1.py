import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc1 = ct.CDLL("./func.so")

class ComplexDouble(ct.Structure):
    _fields_ = [("real", ct.c_double), ("imag", ct.c_double)]

handc1.dot_product.argtypes = [ct.c_double, ct.c_double]
handc1.dot_product.restype = ComplexDouble
ans = handc1.dot_product(-0.5, (3**0.5)/2)

ans_complex = complex(ans.real, ans.imag)

print("Dot product:", ans_complex)
