import numpy as np
from itertools import product

def count_matrices():
    # Step 1: compute squared norm multiplicities for column vectors in {0,1,2}^3
    cols = np.array(list(product((0,1,2), repeat=3)))
    norms = np.sum(cols**2, axis=1)
    unique, counts = np.unique(norms, return_counts=True)
    N = dict(zip(unique, counts))  # N[n] = multiplicity of norm n
    
    # Step 2: sum over all triples of norms that add to 5
    total = 0
    for n1, c1 in N.items():
        for n2, c2 in N.items():
            for n3, c3 in N.items():
                if n1 + n2 + n3 == 5:
                    total += c1 * c2 * c3
    return total, N

if __name__ == "__main__":
    total, N = count_matrices()
    print("Single-column squared norm multiplicities N(n):")
    for n in sorted(N):
        print(f"  n={n}: {N[n]} ways")
    print("\nTotal matrices =", total)
