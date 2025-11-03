import ctypes
import numpy as np
import sympy as sp

def get_plot_data():

    lib = ctypes.CDLL('./code.so')
    out_data = (ctypes.c_double * 4)()
    lib.get_problem_data(out_data)
    a, b, c, r = list(out_data)

    x, y, x0, y0 = sp.symbols('x y x0 y0')
    y0_expr = sp.solve(a*x0 + b*y0 + c, y0)[0]
    chord_on_line = (x*x0 + y*y0 - r**2).subs(y0, y0_expr)
    poly = sp.Poly(chord_on_line, x0)

    eq1 = poly.coeff_monomial(x0)
    eq2 = poly.coeff_monomial(1)

    sol = sp.solve([eq1, eq2], [x, y])
    p_fixed = np.array([float(sol[x]), float(sol[y])])

    p1 = np.array([0.0, 4.0])
    p2 = np.array([2.0, 0.0])

    t1 = np.array([np.sqrt(15)/4, 1/4])
    t2 = np.array([-np.sqrt(15)/4, 1/4])
    t3 = np.array([1/2, np.sqrt(3)/2])
    t4 = np.array([1/2, -np.sqrt(3)/2])

    return {
        "p_fixed": p_fixed,
        "p1": p1, "t1": t1, "t2": t2,
        "p2": p2, "t3": t3, "t4": t4,
        "line_coeffs": (a, b, c)
    }
