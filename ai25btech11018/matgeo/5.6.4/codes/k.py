

import sys
#for path to external scripts
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')
#path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
#from line.funcs import *
#from triangle.funcs import *
#from matrix.funcs import *
#from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

def solve_for_k_cayley_hamilton(A, I):
    """
    Solves for the scalar k in the matrix equation A^2 = kA - 2I
    by using the Cayley-Hamilton Theorem.

    Args:
        A (np.array): A 2x2 NumPy array representing matrix A.
        I (np.array): A 2x2 NumPy array representing the identity matrix I.

    Returns:
        float: The value of k that satisfies the equation.
    """
    # Step 1: Find the characteristic polynomial coefficients of A
    # The characteristic polynomial is lambda^2 - (tr(A))lambda + det(A) = 0
    coeffs = np.poly(A)
    # The coefficients will be [1, -tr(A), det(A)]

    # Step 2: Apply the Cayley-Hamilton Theorem
    # The matrix A satisfies its characteristic equation:
    # A^2 + coeffs[1]*A + coeffs[2]*I = 0
    
    # Rearranging the Cayley-Hamilton equation:
    # A^2 = -coeffs[1]*A - coeffs[2]*I

    # Step 3: Compare with the given equation
    # Given: A^2 = kA - 2I
    # By comparing the coefficients of A and I, we find:
    # k = -coeffs[1]
    # -2 = -coeffs[2]  =>  coeffs[2] = 2

    # The value of k is the negative of the second coefficient from np.poly(A)
    k_value = -coeffs[1]
    
    # Verification check to see if the determinant is correct
    if np.isclose(coeffs[2], 2):
        print("Verification successful: The determinant from the characteristic polynomial matches the problem statement.")
    else:
        print("Verification failed: The determinant does not match the problem statement.")
        
    return k_value

# Given matrices
A = np.array([[3, -2],
              [4, -2]])
I = np.array([[1, 0],
              [0, 1]])

# Find the value of k
k_value = solve_for_k_cayley_hamilton(A, I)

# Print the final result
if k_value is not None:
    print(f"\nThe value of k is: {k_value}")