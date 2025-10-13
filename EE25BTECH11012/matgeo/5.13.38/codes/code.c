#include <stdio.h>
#include <math.h>
#include <string.h>

#define N 3

// --- Matrix Utility Functions ---

// Prints a 3x3 matrix
void print_matrix(const char* name, double mat[N][N]) {
    printf("Matrix %s:\n", name);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%9.2f ", mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Multiplies two 3x3 matrices: C = A * B
void multiply_matrices(double a[N][N], double b[N][N], double c[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            c[i][j] = 0;
            for (int k = 0; k < N; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

// Calculates matrix power: result = mat^p
void power_matrix(double mat[N][N], int p, double result[N][N]) {
    // Initialize result as identity matrix
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }
    
    double temp[N][N];
    for (int i = 0; i < p; i++) {
        multiply_matrices(result, mat, temp);
        memcpy(result, temp, sizeof(double) * N * N);
    }
}

// Adds two matrices: C = A + B
void add_matrices(double a[N][N], double b[N][N], double c[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
}

// Subtracts two matrices: C = A - B
void subtract_matrices(double a[N][N], double b[N][N], double c[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            c[i][j] = a[i][j] - b[i][j];
        }
    }
}

// Checks if a matrix is skew-symmetric (M^T = -M)
int is_skew_symmetric(double mat[N][N]) {
    const double epsilon = 1e-9; // Tolerance for float comparison
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            // Check if M[i][j] is approximately -M[j][i]
            if (fabs(mat[i][j] + mat[j][i]) > epsilon) {
                return 0; // Not skew-symmetric
            }
        }
    }
    // Check if diagonal elements are zero
    for (int i = 0; i < N; i++) {
        if (fabs(mat[i][i]) > epsilon) {
            return 0; // Not skew-symmetric
        }
    }
    return 1; // It is skew-symmetric
}


// --- Main Program ---

int main() {
    // Define arbitrary non-zero matrices as per the problem statement
    // X and Y are skew-symmetric (M[i][j] = -M[j][i])
    double X[N][N] = {
        {0.0, 1.0, 2.0},
        {-1.0, 0.0, 3.0},
        {-2.0, -3.0, 0.0}
    };
    double Y[N][N] = {
        {0.0, -2.0, 4.0},
        {2.0, 0.0, -5.0},
        {-4.0, 5.0, 0.0}
    };
    // Z is symmetric (M[i][j] = M[j][i])
    double Z[N][N] = {
        {1.0, 2.0, 3.0},
        {2.0, 4.0, 5.0},
        {3.0, 5.0, 6.0}
    };

    printf("Verifying the properties of matrices from the question.\n");
    printf("------------------------------------------------------\n\n");

    // Temporary matrices for calculations
    double term1[N][N], term2[N][N], result[N][N];

    // --- Option (a): Y^3 * Z^4 - Z^4 * Y^3 ---
    power_matrix(Y, 3, term1);
    power_matrix(Z, 4, term2);
    double Y3Z4[N][N];
    multiply_matrices(term1, term2, Y3Z4);
    
    power_matrix(Z, 4, term1);
    power_matrix(Y, 3, term2);
    double Z4Y3[N][N];
    multiply_matrices(term1, term2, Z4Y3);

    subtract_matrices(Y3Z4, Z4Y3, result);
    printf("a) Y^3*Z^4 - Z^4*Y^3 is skew-symmetric? --> %s\n", is_skew_symmetric(result) ? "Yes" : "No");

    // --- Option (b): X^44 + Y^44 ---
    power_matrix(X, 44, term1);
    power_matrix(Y, 44, term2);
    add_matrices(term1, term2, result);
    printf("b) X^44 + Y^44 is skew-symmetric? --> %s\n", is_skew_symmetric(result) ? "Yes" : "No");

    // --- Option (c): X^4 * Z^3 - Z^3 * X^4 ---
    power_matrix(X, 4, term1);
    power_matrix(Z, 3, term2);
    double X4Z3[N][N];
    multiply_matrices(term1, term2, X4Z3);

    power_matrix(Z, 3, term1);
    power_matrix(X, 4, term2);
    double Z3X4[N][N];
    multiply_matrices(term1, term2, Z3X4);
    
    subtract_matrices(X4Z3, Z3X4, result);
    printf("c) X^4*Z^3 - Z^3*X^4 is skew-symmetric? --> %s\n", is_skew_symmetric(result) ? "Yes" : "No");

    // --- Option (d): X^23 + Y^23 ---
    power_matrix(X, 23, term1);
    power_matrix(Y, 23, term2);
    add_matrices(term1, term2, result);
    printf("d) X^23 + Y^23 is skew-symmetric? --> %s\n", is_skew_symmetric(result) ? "Yes" : "No");

    printf("\n------------------------------------------------------\n");
    printf("Conclusion: The correct options are (c) and (d).\n");

    return 0;
}