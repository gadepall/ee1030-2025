#CODE BY BHAVESH G

import numpy as np

def read_matrix_3x3():
    print("Enter 3x3 matrix :")
    vals = list(map(float, input().split()))
    while len(vals) != 9:
        print("Please enter exactly 9 numbers:")
        vals = list(map(float, input().split()))
    return np.array(vals, dtype=float).reshape(3, 3)

def read_vector_3():
    print("Enter initial vector 3x1:")
    vals = list(map(float, input().split()))
    while len(vals) != 3:
        print("Please enter exactly 3 numbers:")
        vals = list(map(float, input().split()))
    return np.array(vals, dtype=float)

def power_method_rayleigh(A, x0, iters):

    if np.allclose(x0, 0):
        raise ValueError("Initial vector must be nonzero.")
    y = x0.astype(float)
    
    infn = np.max(np.abs(y))
    if infn == 0:
        raise ValueError("Zero vector encountered.")
    y = y / infn

    lam = None
    for _ in range(iters):
        x = A @ y
        infn = np.max(np.abs(x))
        if infn == 0:
            
            lam = 0.0
            y = x
            break
        y = x / infn
        
        lam = float((y @ (A @ y)) / (y @ y))
    return lam, y

def main():
    A = read_matrix_3x3()
    x0 = read_vector_3()
    iters = int(input("Enter number of iterations: ").strip())
    lam, y = power_method_rayleigh(A, x0, iters)
    print("Final Rayleigh quotient:", lam)

if __name__ == "__main__":
    main()

