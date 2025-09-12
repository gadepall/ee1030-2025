import numpy as np
import itertools

def is_parallel(v, w, tol=1e-9):
    """Check if vectors v and w are parallel (cross product = 0)."""
    v = np.array(v, dtype=float)
    w = np.array(w, dtype=float)
    if np.allclose(v, 0, atol=tol) or np.allclose(w, 0, atol=tol):
        return np.allclose(v, w, atol=tol)
    return np.allclose(np.cross(v, w), 0, atol=tol)

def is_parallelogram(points):
    """
    Check if 4 points form a parallelogram using only the parallel-sides test.
    Returns True if yes, else False.
    """
    P = [np.array(p, dtype=float) for p in points]

    for perm in itertools.permutations(range(4)):
        A, B, C, D = [P[i] for i in perm]

        AB, BC, CD, DA = B - A, C - B, D - C, A - D

        # Check opposite sides are parallel and adjacent sides not parallel
        if is_parallel(AB, CD) and is_parallel(BC, DA) and not is_parallel(AB, BC):
            return True
    return False


# Example points
A = (-1,  2,  1)
B = ( 1, -2,  5)
C = ( 4, -7,  8)
D = ( 2, -3,  4)

points = [A, B, C, D]

