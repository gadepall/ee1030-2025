import ctypes

# Define the C double type
DoubleArray2x2 = ctypes.c_double * 2
Matrix2x2 = DoubleArray2x2 * 2  # 2x2 matrix

def print_matrix(mat):
    for i in range(2):
        print(" |", end='')
        for j in range(2):
            print(f"{mat[i][j]:8.2f}", end='')
        print(" |")

# Initialize matrix A
matrix = Matrix2x2(
    DoubleArray2x2(2.0, 2.0),
    DoubleArray2x2(4.0, 3.0)
)

print("Original Matrix A:")
print_matrix(matrix)

# Step 1: Calculate determinant
det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
if det == 0:
    print("\nInverse does not exist because the determinant is zero.")
    exit(1)

# Step 2: Create augmented matrix [A | I] using ctypes
AugmentedRow = ctypes.c_double * 4
AugmentedMatrix = AugmentedRow * 2

augmented = AugmentedMatrix(
    AugmentedRow(matrix[0][0], matrix[0][1], 1.0, 0.0),
    AugmentedRow(matrix[1][0], matrix[1][1], 0.0, 1.0)
)

# Step 3: Gauss-Jordan Elimination

# Row 1 normalization
pivot1 = augmented[0][0]
for j in range(4):
    augmented[0][j] /= pivot1

# Row 2 elimination
factor1 = augmented[1][0]
for j in range(4):
    augmented[1][j] -= factor1 * augmented[0][j]

# Row 2 normalization
pivot2 = augmented[1][1]
for j in range(4):
    augmented[1][j] /= pivot2

# Row 1 elimination
factor2 = augmented[0][1]
for j in range(4):
    augmented[0][j] -= factor2 * augmented[1][j]

# Step 4: Extract inverse
inverse = Matrix2x2(
    DoubleArray2x2(augmented[0][2], augmented[0][3]),
    DoubleArray2x2(augmented[1][2], augmented[1][3])
)

print("\nFound Inverse Matrix A⁻¹:")
print_matrix(inverse)
