import matplotlib.pyplot as plt

def solve_part_c(p):
    """
    Solves part (c) by checking every matrix of the form [[a, b], [c, a]].

    It counts matrices where:
    1. The determinant (a^2 - bc) is NOT divisible by p.

    Args:
        p: An odd prime number.

    Returns:
        The total count of such matrices.
    """
    count = 0
    # Iterate through all possible values for a, b, and c
    for a in range(p):
        for b in range(p):
            for c in range(p):
                # Determinant condition: a^2 - bc != 0 mod p
                determinant_is_not_zero = (a * a - b * c) % p != 0
                
                if determinant_is_not_zero:
                    count += 1
    return count

def theoretical_c(p):
    """
    Returns the result from the theoretical formula for part (c), p^3 - p^2.
    """
    return p**3 - p**2

# --- Main execution block to run the verification ---
if __name__ == "__main__":
    # Test the solution for a few small odd prime numbers
    test_primes = [3, 5, 7, 11, 13]

    print("--- Verification for Part (c) ---")
    print("Assuming matrix form is A = [[a, b], [c, a]]")
    print("-" * 50)
    print(f"{'Prime (p)':<10} | {'Numerical':<10} | {'Theoretical (p^3-p^2)':<22}")
    print(f"{'----------':<10} | {'----------':<10} | {'----------------------':<22}")

    numerical_results = []
    theoretical_results = []

    for p_val in test_primes:
        num_res = solve_part_c(p_val)
        the_res = theoretical_c(p_val)
        numerical_results.append(num_res)
        theoretical_results.append(the_res)
        
        # Check if the results match and print
        match_status = "Match" if num_res == the_res else "Mismatch"
        print(f"{p_val:<10} | {num_res:<10} | {the_res:<22} ({match_status})")
        
    # --- Plotting the results ---
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 6))
    
    # Plot numerical results as points and theoretical as a line
    plt.plot(test_primes, numerical_results, 'o', markersize=8, color='blue', label='Numerical Count (Brute-Force)')
    plt.plot(test_primes, theoretical_results, 'b--', label='Theoretical Formula: p^3 - p^2')
    
    plt.title('Part (c) Verification: det(A) != 0', fontsize=16)
    plt.xlabel('Prime number (p)', fontsize=12)
    plt.ylabel('Number of Valid Matrices', fontsize=12)
    plt.xticks(test_primes)
    plt.legend(fontsize=11)
    plt.grid(True)
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('figure_c.png')
    print("\nPlot saved as figure_c.png")
    
    plt.show()
