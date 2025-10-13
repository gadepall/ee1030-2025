import math

def compute_line_params(m, d):
    """
    Compute normal vector components A and B,
    and constants C1 and C2 for the line equation:
        Ax + By = ±C

    Parameters:
        m (float): Slope of the line (given)
        d (float): Perpendicular distance from origin

    Returns:
        A (float): Coefficient of x (normal vector x-component)
        B (float): Coefficient of y (normal vector y-component)
        C1 (float): +C value
        C2 (float): -C value
    """
    # Normal vector n = (-m, 1)
    A = -m
    B = 1.0

    # Norm of the normal vector
    norm = math.sqrt(A**2 + B**2)

    # |c| = d * ||n||
    abs_c = d * norm

    # Return both +c and -c
    C1 = abs_c
    C2 = -abs_c

    return A, B, C1, C2


# Example usage
if __name__ == "__main__":
    m = -2 - math.sqrt(3)
    d = 4.0

    A, B, C1, C2 = compute_line_params(m, d)

    print("Equation of the lines:")
    print(f"{A:.4f}x + {B:.4f}y = {C1:.4f}")
    print(f"{A:.4f}x + {B:.4f}y = {C2:.4f}")
