import numpy as np
import sympy as sp

A=np.array([[4,-3],[3,4]])
b=np.array([5,0])
x=np.linalg.solve(A,b)
transform_matrix=sp.Matrix([[x[0],-x[1]],[x[1],x[0]]])
print("The transformation matrix:")
sp.pprint(transform_matrix)
