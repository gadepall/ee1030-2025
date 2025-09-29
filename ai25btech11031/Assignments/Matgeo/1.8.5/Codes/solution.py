import numpy as np

def sphere_from_sum_of_squares(A, B, K):
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    M = (A + B) / 2.0
    diff = A - B
    diff_sq = np.dot(diff, diff)  # ||A-B||^2
    r2 = (2.0 * K**2 - diff_sq) / 4.0
    if r2 < 0:
        return {'center': M, 'r2': r2, 'radius': None, 'real': False}
    else:
        return {'center': M, 'r2': r2, 'radius': np.sqrt(r2), 'real': True}

def main():
    # Input values
    A = tuple(map(float, input("Enter coordinates of A (x y z): ").split()))
    B = tuple(map(float, input("Enter coordinates of B (x y z): ").split()))
    K = float(input("Enter constant K: "))

    res = sphere_from_sum_of_squares(A, B, K)

    print("\n--- Results ---")
    print("Point A =", A)
    print("Point B =", B)
    print("K =", K)
    print("Center M =", res['center'])
    print("r^2 =", res['r2'])

    if res['real']:
        print("Radius =", res['radius'])
        # Vector form of locus
        print("\nEquation of locus (vector form):")
        print(f"|| P - {res['center']} ||^2 = {res['r2']}")
    else:
        print("No real sphere exists (r^2 < 0).")

if __name__ == "__main__":
    main()
