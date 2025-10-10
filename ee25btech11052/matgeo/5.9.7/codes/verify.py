import numpy as np

# System of equations from the problem:
# 1*x + 25*y = 4500
# 1*x + 30*y = 5200

# Setup the matrix 'A' (coefficients of x and y)
A = np.array([[1, 25], 
              [1, 30]])

# Setup the vector 'B' (the constant values)
B = np.array([4500, 5200])

# --- Solve the system of linear equations ---
# This is the most direct and efficient way to solve for the variables (x, y)
# It solves the matrix equation A*x = B

# A matrix has a unique solution if its determinant is non-zero.
determinant = np.linalg.det(A)

if determinant != 0:
    solution = np.linalg.solve(A, B)

    # The solution array contains the values for x and y
    fixed_charge = solution[0]
    cost_per_day = solution[1]

    print("--- Solution ---")
    print(f"The fixed monthly charge (x) is: ₹{fixed_charge:.0f}")
    print(f"The cost of food per day (y) is: ₹{cost_per_day:.0f}")
    print("\nThis matches the solution in your document.")
else:
    print("Could not solve the system of equations. The matrix is singular (determinant is zero).")

