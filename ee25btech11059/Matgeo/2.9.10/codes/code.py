import numpy as np

EPS = 1e-6

def dot2(a, b):
    """Compute dot product of two 2D vectors"""
    return np.dot(a, b)

def solve_matrix_vectors(a0, a1, b0, b1):
    """
    Returns True if (a + 2b) is perpendicular to a under the condition ||a + b|| == ||b||, else False
    """
    a_vec = np.array([a0, a1])
    b_vec = np.array([b0, b1])

    ab_vec = a_vec + b_vec          # a + b
    b_norm2 = dot2(b_vec, b_vec)    # ||b||^2
    ab_norm2 = dot2(ab_vec, ab_vec) # ||a + b||^2

    if abs(ab_norm2 - b_norm2) > EPS:
        # Condition ||a + b|| == ||b|| fails
        return False

    a2b_vec = a_vec + 2.0 * b_vec   # a + 2b
    dp = dot2(a_vec, a2b_vec)       # a · (a + 2b)

    return abs(dp) < EPS

# Example usage:
if __name__ == "__main__":
    a0, a1 = 1.0, 2.0
    b0, b1 = -1.0, 1.0
    if solve_matrix_vectors(a0, a1, b0, b1):
        print("Condition satisfied: (a + 2b) is perpendicular to a")
    else:
        print("Condition NOT satisfied")

