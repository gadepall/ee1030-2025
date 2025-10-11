from ctypes import c_double

def solve_linear_system():
    # Coefficients and constants from the equations
    a1 = c_double(2.0)
    b1 = c_double(1.0)
    c1 = c_double(5.0)

    a2 = c_double(3.0)
    b2 = c_double(2.0)
    c2 = c_double(8.0)

    # Calculate the determinant
    determinant = c_double(a1.value * b2.value - a2.value * b1.value)

    if determinant.value != 0:
        # Use Cramer's Rule
        x = c_double((c1.value * b2.value - c2.value * b1.value) / determinant.value)
        y = c_double((a1.value * c2.value - a2.value * c1.value) / determinant.value)

        # Print the results
        print("The solution is:")
        print(f"x = {x.value:.2f}")
        print(f"y = {y.value:.2f}")
    else:
        print("The system does not have a unique solution.")

# Run the function
solve_linear_system()
