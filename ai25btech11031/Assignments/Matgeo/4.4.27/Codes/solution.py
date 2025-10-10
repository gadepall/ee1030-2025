import numpy as np

def solve_for_x(A, C, D):
    # Convert to numpy arrays
    A, C, D = np.array(A), np.array(C), np.array(D)

    # Step 1: compute vectors AC and AD
    AC = C - A
    AD = D - A

    # Step 2: normal vector n = AC × AD
    n = np.cross(AC, AD)

    # Step 3: vector (B-A) = (1, x-2, 4)
    # Dot product condition: n · (B-A) = 0
    coeff_x = n[1]
    constant = n[0]*1 + n[1]*(-2) + n[2]*4

    x = -constant / coeff_x
    return x

# ---- Main Program ----
if __name__ == "__main__":
    # Take inputs
    A = list(map(float, input("Enter coordinates of A (x y z): ").split()))
    C = list(map(float, input("Enter coordinates of C (x y z): ").split()))
    D = list(map(float, input("Enter coordinates of D (x y z): ").split()))

    x_value = solve_for_x(A, C, D)
    print("The value of x such that A, B, C, D are coplanar is:", round(x_value, 2))

