#include <stdio.h>
#include <math.h> // Required for fabs() for floating-point comparisons

// --- Function Prototypes ---
void printMatrix(const char* name, double matrix[2][2]);
double determinant(double matrix[2][2]);
void transpose(double in[2][2], double out[2][2]);
int inverse(double in[2][2], double out[2][2]); // Returns 1 on success, 0 on failure
int areMatricesEqual(double A[2][2], double B[2][2]);

int main() {
    // Define the 2x2 matrix Q
    double Q[2][2] = {{1.0, -2.0}, {2.0, 1.0}};

    printf("Given Matrix Q:\n");
    printMatrix("Q", Q);
    // a) Check if Q is equal to its transpose.
    printf("a) Checking if Q == Q^T ...\n");
    double Q_T[2][2];
    transpose(Q, Q_T);
    printMatrix("Transpose Q^T", Q_T);
    printf("Result: Statement (a) is %s.\n\n", areMatricesEqual(Q, Q_T) ? "TRUE" : "FALSE");

    // b) Check if Q is equal to its inverse.
    printf("b) Checking if Q == Q^-1 ...\n");
    double Q_inv[2][2];
    if (inverse(Q, Q_inv)) { // Check if inverse exists before using it
        printMatrix("Inverse Q^-1", Q_inv);
        printf("Result: Statement (b) is %s.\n\n", areMatricesEqual(Q, Q_inv) ? "TRUE" : "FALSE");
    } else {
        printf("Inverse does not exist.\n");
        printf("Result: Statement (b) is FALSE.\n\n");
    }

    // c) & d) Check for full rank and column dependency using the determinant.
    printf("c/d) Checking rank and column dependency...\n");
    double det = determinant(Q);
    printf("Determinant of Q = %.2f\n", det);

    // If determinant is non-zero, it has full rank and independent columns.
    if (fabs(det) > 1e-9) {
        printf("Result: Statement (c) is TRUE (Determinant is non-zero, so Q is of full rank).\n");
        printf("Result: Statement (d) is FALSE (Columns are linearly independent).\n\n");
    } else {
        printf("Result: Statement (c) is FALSE (Determinant is zero, so Q is not of full rank).\n");
        printf("Result: Statement (d) is TRUE (Columns are linearly dependent).\n\n");
    }
    printf("Conclusion: The only TRUE statement is (c).\n");

    return 0;
}

void printMatrix(const char* name, double matrix[2][2]) {
    printf("%s = \n", name);
    printf("  | %6.2f  %6.2f |\n", matrix[0][0], matrix[0][1]);
    printf("  | %6.2f  %6.2f |\n", matrix[1][0], matrix[1][1]);
}

double determinant(double matrix[2][2]) {
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
}

void transpose(double in[2][2], double out[2][2]) {
    out[0][0] = in[0][0];
    out[0][1] = in[1][0];
    out[1][0] = in[0][1];
    out[1][1] = in[1][1];
}

int inverse(double in[2][2], double out[2][2]) {
    double det = determinant(in);

    // A matrix is invertible if and only if its determinant is non-zero.
    if (fabs(det) < 1e-9) {
        return 0; // No inverse exists
    }

    double inv_det = 1.0 / det;
    out[0][0] =  in[1][1] * inv_det;
    out[0][1] = -in[0][1] * inv_det;
    out[1][0] = -in[1][0] * inv_det;
    out[1][1] =  in[0][0] * inv_det;

    return 1; // Success
}

int areMatricesEqual(double A[2][2], double B[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            // Use a small tolerance for floating-point comparison
            if (fabs(A[i][j] - B[i][j]) > 1e-9) {
                return 0; // Not equal
            }
        }
    }
    return 1; // Equal
}