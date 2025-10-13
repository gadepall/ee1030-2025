# call.py
import ctypes
import sympy

def find_locus_equation():
    lib = ctypes.CDLL('./code.so')

    double_array_3 = ctypes.c_double * 3
    lib.get_circle_params.argtypes = [ctypes.POINTER(ctypes.c_double)]
    out_data_c = double_array_3()

    lib.get_circle_params(out_data_c)
    c1_x, c1_y, r1 = list(out_data_c)  # c1_x=3.0, c1_y=3.0, r1=2.0

    # Symbols: h,k for centre of variable circle
    h, k = sympy.symbols('h k', real=True)

    # We take external tangency and assume h >= 0 => r = h
    r = h

    lhs = (h - c1_x)**2 + (k - c1_y)**2
    rhs = (r + r1)**2

    equation = sympy.Eq(lhs, rhs)
    locus_expr = sympy.simplify(equation.lhs - equation.rhs)

    # Rename symbols to conventional x,y for the returned equation
    x, y = sympy.symbols('x y', real=True)
    final_locus = sympy.simplify(locus_expr.subs({h: x, k: y}))

    return sympy.Eq(final_locus, 0)

if __name__ == '__main__':
    eq = find_locus_equation()
    print("Derived locus equation:", eq)

