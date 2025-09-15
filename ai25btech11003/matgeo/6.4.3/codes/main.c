
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to multiply matrices
void matrix_multiply(double a[2][2], double b[2][1], double result[2][1]) {
    for (int i = 0; i < 2; i++) {
        result[i][0] = 0;
        for (int j = 0; j < 2; j++) {
            result[i][0] += a[i][j] * b[j][0];
        }
    }
}

// Function to solve 2x2 linear system using Gaussian elimination
void solve_linear_system(double A[2][2], double b[2], double x[2]) {
    // Create augmented matrix
    double aug[2][3];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            aug[i][j] = A[i][j];
        }
        aug[i][2] = b[i];
    }

    // Forward elimination
    // Make aug[0][0] = 1
    double factor = aug[0][0];
    for (int j = 0; j < 3; j++) {
        aug[0][j] /= factor;
    }

    // Make aug[1][0] = 0
    factor = aug[1][0];
    for (int j = 0; j < 3; j++) {
        aug[1][j] -= factor * aug[0][j];
    }

    // Make aug[1][1] = 1
    factor = aug[1][1];
    for (int j = 0; j < 3; j++) {
        aug[1][j] /= factor;
    }

    // Back substitution
    // Make aug[0][1] = 0
    factor = aug[0][1];
    for (int j = 0; j < 3; j++) {
        aug[0][j] -= factor * aug[1][j];
    }

    x[0] = aug[0][2];
    x[1] = aug[1][2];
}

int main() {
    // Define points and direction vectors from the PDF
    double A[3] = {2, -5, 1};
    double B[3] = {7, 0, -6};
    double dir1[3] = {3, 2, 6};
    double dir2[3] = {1, 2, 2};

    // Calculate B - A
    double B_minus_A[3];
    for (int i = 0; i < 3; i++) {
        B_minus_A[i] = B[i] - A[i];
    }

    // Create matrix M = [dir1, dir2] (3x2)
    double M[3][2] = {{dir1[0], dir2[0]}, {dir1[1], dir2[1]}, {dir1[2], dir2[2]}};

    // Calculate M^T * M (2x2)
    double MTM[2][2];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            MTM[i][j] = 0;
            for (int k = 0; k < 3; k++) {
                MTM[i][j] += M[k][i] * M[k][j];
            }
        }
    }

    // Calculate M^T * (B - A) (2x1)
    double MT_B_minus_A[2];
    for (int i = 0; i < 2; i++) {
        MT_B_minus_A[i] = 0;
        for (int j = 0; j < 3; j++) {
            MT_B_minus_A[i] += M[j][i] * B_minus_A[j];
        }
    }

    // Solve (M^T * M) * K = M^T * (B - A)
    double K[2];
    solve_linear_system(MTM, MT_B_minus_A, K);

    double k1 = K[0];
    double k2 = -K[1];  // Because we need -k2 in the original formulation

    // Calculate points x1 and x2
    double x1[3], x2[3];
    for (int i = 0; i < 3; i++) {
        x1[i] = A[i] + k1 * dir1[i];
        x2[i] = B[i] + k2 * dir2[i];
    }

    // Calculate distance ||x2 - x1||
    double diff[3];
    double distance_squared = 0;
    for (int i = 0; i < 3; i++) {
        diff[i] = x2[i] - x1[i];
        distance_squared += diff[i] * diff[i];
    }
    double distance = sqrt(distance_squared);

    // Write results to main.dat
    FILE *fp = fopen("main.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "k1: %.10f\n", k1);
    fprintf(fp, "k2: %.10f\n", k2);
    fprintf(fp, "x1: %.10f %.10f %.10f\n", x1[0], x1[1], x1[2]);
    fprintf(fp, "x2: %.10f %.10f %.10f\n", x2[0], x2[1], x2[2]);
    fprintf(fp, "distance: %.10f\n", distance);
    fprintf(fp, "exact_distance: 17*sqrt(5)/5\n");

    fclose(fp);

    printf("Results written to main.dat\n");
    printf("k1 = %.6f, k2 = %.6f\n", k1, k2);
    printf("Distance = %.6f\n", distance);
    printf("Exact distance = 17*sqrt(5)/5 = %.6f\n", 17*sqrt(5)/5);

    return 0;
}
