import numpy as np

# Set the size of the matrices
n = 3

# --- Step 1: Create the necessary matrices ---

# Create a random n x n nonsingular matrix R.
# A random matrix is almost certain to be nonsingular.
R = np.random.rand(n, n)
print(f"Matrix R:\n{R}\n")

# Calculate its inverse
R_inv = np.linalg.inv(R)
print(f"Inverse of R (R⁻¹):\n{R_inv}\n")

# Create a random n x n matrix P
P = np.array([[2, 0, 0], [0, 3, 4], [0, 4, 9]])
print(f"Matrix P:\n{P}\n")

# --- Step 2: Find eigenvalues and eigenvectors of P ---

eigenvalues, eigenvectors = np.linalg.eig(P)

# Let's pick the first eigenvalue (λ) and its corresponding eigenvector (x)
# Note: The problem specifies a non-zero eigenvalue.
lambda_p = eigenvalues[0]
x = eigenvectors[:, 0]

print(f"Eigenvalues of P: {eigenvalues}")
print(f"Selected eigenvalue (λ) of P: {lambda_p:.4f}")
print(f"Corresponding eigenvector (x) of P:\n{x}\n")

# --- Step 3: Verify that Px = λx ---

# Calculate Px
Px = np.dot(P, x)
# Calculate λx
lambda_x = lambda_p * x

print(f"Verification Check:")
print(f"P * x      = {Px}")
print(f"λ * x      = {lambda_x}")
# Use np.allclose for safe floating-point comparison
print(f"Is Px ≈ λx?  {np.allclose(Px, lambda_x)}\n")


# --- Step 4: Calculate Q using the similarity transformation ---

# Q = R⁻¹ * P * R
Q = np.dot(R_inv, np.dot(P, R))
print(f"Matrix Q (calculated as R⁻¹PR):\n{Q}\n")


# --- Step 5: Test the given options from the question ---

print("--- Testing the Options ---")

# Option a) Rx is an eigenvector of Q corresponding to eigenvalue λ
y1 = np.dot(R, x)
Q_y1 = np.dot(Q, y1)
lambda_y1 = lambda_p * y1
print(f"a) Is Q(Rx) ≈ λ(Rx)?  {np.allclose(Q_y1, lambda_y1)}")
print(f"   Q(Rx) = {Q_y1}")
print(f"   λ(Rx) = {lambda_y1}\n")


# Option c) R⁻¹x is an eigenvector of Q corresponding to eigenvalue λ
y2 = np.dot(R_inv, x)
Q_y2 = np.dot(Q, y2)
lambda_y2 = lambda_p * y2
print(f"c) Is Q(R⁻¹x) ≈ λ(R⁻¹x)?  {np.allclose(Q_y2, lambda_y2)}")
print(f"   Q(R⁻¹x) = {Q_y2}")
print(f"   λ(R⁻¹x) = {lambda_y2}\n")

# Note: Since we found the correct answer, we don't need to test b and d,
# but a full test would show they are also false.

print("Conclusion: The code demonstrates that option (c) is the correct answer.")

