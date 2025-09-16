import ctypes
import sympy as sp

lib = ctypes.CDLL("./libref_solver.so")
lib.solve_ref.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int)]

result = (ctypes.c_double * 9)()
rank = ctypes.c_int()

# Call C function
lib.solve_ref(result, ctypes.byref(rank))

# Convert to SymPy Matrix for pretty output
ref = sp.Matrix(3, 3, result)
print("Row Echelon Form (REF):")
sp.pprint(ref)
print("\nRank of matrix:", rank.value)


