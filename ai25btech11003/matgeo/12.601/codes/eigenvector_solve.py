#CODE BY BHAVESH G
import numpy as np

print("Eigenvalue Problem Solver")
print("========================")

n = int(input("Matrix size (n): "))

print(f"Enter {n}x{n} matrix (row by row):")
matrix = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix.append(row)

A = np.array(matrix)
print("\nMatrix A:")
print(A)


lam = float(input("\nEigenvalue: "))

I = np.eye(n)
B = A - lam * I


eigenvals, eigenvecs = np.linalg.eig(A)

closest_idx = np.argmin(np.abs(eigenvals - lam))
eigenvector = eigenvecs[:, closest_idx].real

if abs(eigenvector[0]) > 1e-10:
    eigenvector = eigenvector / eigenvector[0]
    eigenvector = np.round(eigenvector, 6)

print(f"\nEigenvector for λ = {lam}:")
print(eigenvector)
