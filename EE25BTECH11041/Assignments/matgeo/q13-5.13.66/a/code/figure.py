import matplotlib.pyplot as plt

def solve_part_a(p):
    """
    Solves part (a) by checking every possible matrix of the form [[a, b], [c, a]].

    It counts the number of matrices where:
    1. The determinant (a^2 - bc) is divisible by p.
    2. The matrix is either symmetric (c=b) or skew-symmetric (a=0, c=-b).

    Args:
        p: An odd prime number.

    Returns:
        The total count of such matrices.
    """
    # A set is used to store unique matrices. This is important because the
    # zero matrix is both symmetric and skew-symmetric, and we must not
    # double-count it. We store a string representation of each matrix.
    valid_matrices = set()

    # Iterate through all possible values for a, b, and c
    for a in range(p):
        for b in range(p):
            for c in range(p):
                # Condition 1: Determinant is divisible by p
                determinant = a**2 - b * c
                if determinant % p == 0:
                    # Condition 2: Matrix is either symmetric or skew-symmetric
                    is_symmetric = (c == b)
                    # For skew-symmetric, c = -b mod p. In Python, (-b % p) handles this correctly.
                    is_skew_symmetric = (a == 0 and c == (-b % p))

                    if is_symmetric or is_skew_symmetric:
                        matrix_str = f"[[{a}, {b}], [{c}, {a}]]"
                        valid_matrices.add(matrix_str)

    return len(valid_matrices)

def theoretical_a(p):
    """Returns the result from the theoretical formula for part (a)."""
    return 2 * p - 1

# --- Main execution block to run the verification ---
if __name__ == "__main__":
    # Test the solution for a few small odd prime numbers
    test_primes = [3, 5, 7, 11, 13]

    print("--- Verification for Part (a) ---")
    print("Assuming matrix form is A = [[a, b], [c, a]]")
    print("-" * 35)
    print(f"{'Prime (p)':<10} | {'Numerical':<10} | {'Theoretical':<12}")
    print(f"{'----------':<10} | {'----------':<10} | {'------------':<12}")

    numerical_results = []
    theoretical_results = []

    for p_val in test_primes:
        num_res = solve_part_a(p_val)
        the_res = theoretical_a(p_val)
        numerical_results.append(num_res)
        theoretical_results.append(the_res)
        
        # Check if the results match and print
        match_status = "Match" if num_res == the_res else "Mismatch"
        print(f"{p_val:<10} | {num_res:<10} | {the_res:<12} ({match_status})")
        
    # --- Plotting the results ---
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 6))
    
    # Plot numerical results as points and theoretical as a line
    plt.plot(test_primes, numerical_results, 'o', markersize=8, label='Numerical Count (Brute-Force)')
    plt.plot(test_primes, theoretical_results, 'r--', label='Theoretical Formula: 2p - 1')
    
    plt.title('Part (a) Verification: Numerical vs. Theoretical', fontsize=16)
    plt.xlabel('Prime number (p)', fontsize=12)
    plt.ylabel('Number of Valid Matrices', fontsize=12)
    plt.xticks(test_primes)
    plt.legend(fontsize=11)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("figure.png", dpi=200)
    plt.show()

