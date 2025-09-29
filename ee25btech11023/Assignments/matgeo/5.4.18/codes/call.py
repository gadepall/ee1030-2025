import ctypes
import sympy
 
lib = ctypes.CDLL('./code.so')

double_array_7 = ctypes.c_double * 7
lib.get_system_coeffs.argtypes = [ctypes.POINTER(ctypes.c_double)]
    
out_data_c = double_array_7()
lib.get_system_coeffs(out_data_c)
    
 
coeffs = list(int(v) for v in out_data_c)
 
M = sympy.Matrix([
        [coeffs[0],  coeffs[1]],  
        [ coeffs[2],  coeffs[3]],  
            ])
K=M.inv()
print(K)