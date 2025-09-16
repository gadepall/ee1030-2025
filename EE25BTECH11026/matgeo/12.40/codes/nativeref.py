import sympy as sp

A=sp.Matrix([[2,3,7],[6,4,7],[4,6,14]])

ref_A=A.echelon_form()
print("Row Echelon Form:")
sp.pprint(ref_A)
rank=A.rank()
print("Rank of the matrix=",rank)
