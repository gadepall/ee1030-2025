import ctypes
import sympy

def find_locus_equation():
     
    lib = ctypes.CDLL('./code.so')
   
    double_array_3 = ctypes.c_double * 3
    lib.get_circle_params.argtypes = [ctypes.POINTER(ctypes.c_double)]
    out_data_c = double_array_3()
    lib.get_circle_params(out_data_c)
     
    c1_x, c1_y, r1 = list(out_data_c)
    c1_center = [c1_x, c1_y]
    print(c1_center)
 
    h, k = sympy.symbols('h k', real=True)
 
    r = sympy.Abs(k)
     
    lhs = (h - c1_center[0])**2 + (k - c1_center[1])**2
    rhs = (r + r1)**2
    
    locus_eq = sympy.simplify(lhs - rhs)
    x, y = sympy.symbols('x y')
    final_locus = locus_eq.subs([(h, x), (k, y)])
    
    return sympy.Eq(final_locus, 0)
