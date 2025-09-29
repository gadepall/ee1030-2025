import ctypes
import numpy as np
import math

lib=ctypes.CDLL("./libexpression.so")

#defining the ctypes arrays
DoubleArray3 = ctypes.c_double * 3
DoubleMatrix3 = (DoubleArray3) * 3

#function parameters
lib.gram_matrix.argtypes = [DoubleArray3, DoubleArray3, DoubleArray3, DoubleMatrix3]
lib.det3.argtypes = [DoubleMatrix3]
lib.det3.restype = ctypes.c_double

#define gram metrices
G_1=DoubleMatrix3()
G_2=DoubleMatrix3()
G_3=DoubleMatrix3()

#define python arrays
a=np.array([1,0,0])
b=np.array([0,1,0])
c=np.array([0,0,1])

# Convert to C arrays
A = DoubleArray3(*a)
B = DoubleArray3(*b)
C = DoubleArray3(*c)

lib.gram_matrix(A, B, C, G_1)
lib.gram_matrix(B, A, C, G_2)
lib.gram_matrix(C, A, B, G_3)

#get det G
mag_1 = math.sqrt(lib.det3(G_1))
mag_2 = math.sqrt(lib.det3(G_2))
mag_3 = math.sqrt(lib.det3(G_3))

# --- Step 4: Compute sign using det(A)
A_mat = np.column_stack((a, b, c))   # matrix [a b c]
sign_a = np.linalg.det(A_mat)      # NumPy to check sign

B_mat = np.column_stack((b, a, c))
sign_b = np.linalg.det(B_mat)

C_mat = np.column_stack((c, a, b))
sign_c = np.linalg.det(C_mat)

print("final value of expression is: ",sign_a*mag_1 + sign_b*mag_2 + sign_c*mag_3)
