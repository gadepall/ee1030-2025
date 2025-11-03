import math #for mathematical functions like sqrt

def condition_number(A):  #defining function
    # Step 1: Compute ATA = A^T * A
    ATA = [[0, 0], [0, 0]]
    ATA[0][0] = A[0][0] * A[0][0] + A[1][0] * A[1][0]
    ATA[0][1] = A[0][0] * A[0][1] + A[1][0] * A[1][1]
    ATA[1][0] = ATA[0][1]  # symmetric
    ATA[1][1] = A[0][1] * A[0][1] + A[1][1] * A[1][1]

    # Step 2: Eigenvalues of 2x2 symmetric matrix
    trace = ATA[0][0] + ATA[1][1]
    det = ATA[0][0] * ATA[1][1] - ATA[0][1] * ATA[1][0]

    disc = trace * trace - 4 * det
    if disc < 0:
        disc = 0  # safeguard against negative due to roundoff

    lambda1 = (trace + math.sqrt(disc)) / 2.0
    lambda2 = (trace - math.sqrt(disc)) / 2.0

    # Step 3: Singular values = sqrt(eigenvalues)
    sigma1 = math.sqrt(lambda1)
    sigma2 = math.sqrt(lambda2)

    # Step 4: Condition number = sigma_max / sigma_min
    sigma_max = max(sigma1, sigma2)
    sigma_min = min(sigma1, sigma2)

    if sigma_min == 0:
        return math.inf  # singular matrix
    return sigma_max / sigma_min


# Example matrix A = [[2, 1], [0, 3]]
A = [[2, 1],
     [0, 3]]

cond_num = condition_number(A)
print(f"Condition number of A: {cond_num}")

