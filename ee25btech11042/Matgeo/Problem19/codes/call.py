
import ctypes


solver_lib = ctypes.CDLL('./12.55.so')


find_x_func = solver_lib.find_orthogonal_x


find_x_func.restype = ctypes.c_float



result = find_x_func()


print(f"The value of x calculated by the C function is: {result}")
print(f"(Which is {result:.2f} or 4/5)")
