import ctypes
import sympy

def solve_number_problem():

    lib = ctypes.CDLL('./code.so')
    double_array_6 = ctypes.c_double * 6
    # The C function will fill an array of 6 doubles
    lib.get_system_coeffs.argtypes = [ctypes.POINTER(ctypes.c_double)]
    
    out_data_c = double_array_6()
    lib.get_system_coeffs(out_data_c)
    
    # Unpack the raw coefficient data from C
    m_coeffs = list(int(v) for v in out_data_c)[:4]
    c_coeffs = list(int(v) for v in out_data_c)[4:]
   
    aug_M = sympy.Matrix([
        [m_coeffs[0], m_coeffs[1], c_coeffs[0]],
        [m_coeffs[2], m_coeffs[3], c_coeffs[1]]
    ])
    print("Initial Augmented Matrix:\n", aug_M)
    rref_matrix, _ = aug_M.rref()
    print("\nReduced Row Echelon Form:\n", rref_matrix)
    
    x_digit = rref_matrix[0, 2]
    y_digit = rref_matrix[1, 2]
    
    return int(x_digit), int(y_digit)


x, y = solve_number_problem()
    
    # Calculate the final two-digit number
number = 10 * x + y

print(f"The number is: {number}")
