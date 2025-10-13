import ctypes
import sympy
 
lib = ctypes.CDLL('./code.so')
 
double_array_7 = ctypes.c_double * 7
lib.get_system_coeffs.argtypes = [ctypes.POINTER(ctypes.c_double)]
    
out_data_c = double_array_7()
lib.get_system_coeffs(out_data_c)
    
 
coeffs = list(int(v) for v in out_data_c)
 
k = sympy.Symbol('k')
    
M = sympy.Matrix([
        [coeffs[0], -k,         coeffs[1]],  
        [k,         coeffs[2],  coeffs[3]],  
        [coeffs[4], coeffs[5],  coeffs[6]]  
    ])
det_M = M.det()
print(f"\nDeterminant = {det_M}")
    
     
solutions = sympy.solve(det_M, k)

print(f"k can be {solutions}")
