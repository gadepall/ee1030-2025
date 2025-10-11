import sympy as sp

def main():
    n = int(input("Enter matrix size n: "))
    print(f"Enter the {n}×{n} matrix row by row (space-separated):")
    mat = []
    for _ in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            raise ValueError("Each row must have n entries.")
        mat.append(row)

    # Construct symbolic matrix and compute characteristic polynomial
    A = sp.Matrix(mat)
    λ = sp.symbols('λ')
    charpoly = A.charpoly(λ).as_expr()

    print("\nThe characteristic equation is:")
    print(sp.simplify(charpoly), "= 0")

if __name__ == "__main__":
    main()

