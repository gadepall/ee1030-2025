import numpy as np

def compute_c_from_a_b_k(a, b, k, tol=1e-9):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)

    if np.linalg.norm(a) < tol:
        raise ValueError("Vector a is (nearly) zero — no unique solution.")
    # For b = a x c, b must be perpendicular to a:
    if abs(np.dot(a, b)) > 1e-8:
        raise ValueError("Inconsistent input: a·b must be 0 for b = a × c.")

    a_cross_b = np.cross(a, b)
    denom = np.dot(a, a)   # |a|^2, guaranteed > 0 here
    c = (a * k - a_cross_b) / denom
    return c

def parse_vec(s):
    vals = list(map(float, s.strip().split()))
    if len(vals) != 3:
        raise ValueError("Please enter exactly 3 numbers for a vector.")
    return vals

def main():
    try:
        a = parse_vec(input("Enter vector a (3 values separated by space): "))
        b = parse_vec(input("Enter vector b (3 values separated by space): "))
        k = float(input("Enter the value of a·c (scalar k): "))
        c = compute_c_from_a_b_k(a, b, k)
    except Exception as e:
        print("Error:", e)
        return

    print("\nComputed c =", c)
    # verification (numerical tolerance)
    print("Verify a × c =", np.cross(a, c))
    print("Given b       =", np.array(b, dtype=float))
    print("Verify a · c =", np.dot(a, c), "(should equal k =", k, ")")

if __name__ == "__main__":
    main()

