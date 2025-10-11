import matplotlib.pyplot as plt

def solve_part_b(p):
    """
    Solves part (b) by checking every matrix of the form [[a, b], [c, a]].

    It counts matrices where:
    1. The trace (2a) is not divisible by p.
    2. The determinant (a^2 - bc) is divisible by p.

    Args:
        p: An odd prime number.

    Returns:
        The total count of such matrices.
    """
    count = 0
    for a in range(p):
        for b in range(p):
            for c in range(p):
                # Trace condition: 2a != 0 mod p => a != 0 (since p is odd)
                trace_is_not_zero = (a != 0)
                
                # Determinant condition: a^2 - bc == 0 mod p
                determinant_is_zero = (a * a - b * c) % p == 0
                
                if trace_is_not_zero and determinant_is_zero:
                    count += 1
    return count

def theoretical_b(p):
    """
    Returns the result from the theoretical formula for part (b), (p-1)^2.
    """
    return (p - 1)**2

# --- Main execution block to run the verification ---
if __name__ == "__main__":
    # Test the solution for a few small odd prime numbers
    test_primes = [3, 5, 7, 11, 13]

    print("--- Verification for Part (b) ---")
    print("Assuming matrix form is A = [[a, b], [c, a]]")
    print("-" * 50)
    print(f"{'Prime (p)':<10} | {'Numerical':<10} | {'Theoretical ((p-1)^2)':<22}")
    print(f"{'----------':<10} | {'----------':<10} | {'----------------------':<22}")

    numerical_results = []
    theoretical_results = []

    for p_val in test_primes:
        num_res = solve_part_b(p_val)
        the_res = theoretical_b(p_val)
        numerical_results.append(num_res)
        theoretical_results.append(the_res)
        
        # Check if the results match and print
        match_status = "Match" if num_res == the_res else "Mismatch"
        print(f"{p_val:<10} | {num_res:<10} | {the_res:<22} ({match_status})")
        
    # --- Plotting the results ---
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 6))
    
    # Plot numerical results as points and theoretical as a line
    plt.plot(test_primes, numerical_results, 'o', markersize=8, color='green', label='Numerical Count (Brute-Force)')
    plt.plot(test_primes, theoretical_results, 'g--', label='Theoretical Formula: (p - 1)^2')
    
    plt.title('Part (b) Verification: det(A) is and tr(A) is not divisible by p', fontsize=16)
    plt.xlabel('Prime number (p)', fontsize=12)
    plt.ylabel('Number of Valid Matrices', fontsize=12)
    plt.xticks(test_primes)
    plt.legend(fontsize=11)
    plt.grid(True)
    plt.tight_layout()
    
    # Save the figure
    plt.savefig('figure_b.png')
    print("\nPlot saved as figure_b.png")
    
    plt.show()

