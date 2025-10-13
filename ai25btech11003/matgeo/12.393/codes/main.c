// orthonormal_solver.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Function to solve orthonormal matrix problem
void solve_orthonormal_matrix() {
    double sqrt_3 = sqrt(3.0);
    double sqrt_2 = sqrt(2.0);
    double sqrt_6 = sqrt(6.0);

    // Mathematical solution:
    // For Q^T * Q = I, we need:
    // 1. a + b + c = 0  (orthogonality constraint)
    // 2. a - c = 0      (orthogonality constraint)
    // 3. a² + b² + c² = 1 (normalization constraint)

    // From constraints: a = c, b = -2a, 6a² = 1
    // Therefore: a = ±1/√6

    double a1 = 1.0 / sqrt_6;
    double b1 = -2.0 / sqrt_6;
    double c1 = 1.0 / sqrt_6;

    double a2 = -1.0 / sqrt_6;
    double b2 = 2.0 / sqrt_6;
    double c2 = -1.0 / sqrt_6;

    printf("Solving Orthonormal Matrix Problem\n");
    printf("==================================\n");
    printf("Solution 1: a = %.6f, b = %.6f, c = %.6f\n", a1, b1, c1);
    printf("Solution 2: a = %.6f, b = %.6f, c = %.6f\n", a2, b2, c2);

    // Create main.so file (binary data)
    FILE *so_file = fopen("main.so", "wb");
    if (so_file != NULL) {
        double solutions[6] = {a1, b1, c1, a2, b2, c2};
        fwrite(solutions, sizeof(double), 6, so_file);
        fclose(so_file);
        printf("\nBinary data written to main.so\n");
    } else {
        printf("Error creating main.so file\n");
    }

    // Create main.dat file (text data)
    FILE *dat_file = fopen("main.dat", "w");
    if (dat_file != NULL) {
        fprintf(dat_file, "# Orthonormal Matrix Solutions\n");
        fprintf(dat_file, "# Solution 1: a, b, c\n");
        fprintf(dat_file, "%.12f %.12f %.12f\n", a1, b1, c1);
        fprintf(dat_file, "# Solution 2: a, b, c\n");
        fprintf(dat_file, "%.12f %.12f %.12f\n", a2, b2, c2);
        fclose(dat_file);
        printf("Text data written to main.dat\n");
    } else {
        printf("Error creating main.dat file\n");
    }
}

// Function to verify orthonormal property
void verify_solution(double a, double b, double c, int solution_num) {
    double sqrt_3 = sqrt(3.0);
    double sqrt_2 = sqrt(2.0);

    // Construct matrix Q
    double Q[3][3] = {
        {1.0/sqrt_3, 1.0/sqrt_2, a},
        {1.0/sqrt_3, 0.0, b},
        {1.0/sqrt_3, -1.0/sqrt_2, c}
    };

    // Calculate Q^T * Q
    double QTQ[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            QTQ[i][j] = 0.0;
            for (int k = 0; k < 3; k++) {
                QTQ[i][j] += Q[k][i] * Q[k][j];
            }
        }
    }

    printf("\nVerification for Solution %d:\n", solution_num);
    printf("Q^T * Q =\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%8.5f ", QTQ[i][j]);
        }
        printf("\n");
    }

    // Check if it's close to identity matrix
    double tolerance = 1e-10;
    int is_identity = 1;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            double expected = (i == j) ? 1.0 : 0.0;
            if (fabs(QTQ[i][j] - expected) > tolerance) {
                is_identity = 0;
            }
        }
    }

    printf("Is orthonormal: %s\n", is_identity ? "Yes" : "No");
}

int main() {
    solve_orthonormal_matrix();

    // Verify both solutions
    double sqrt_6 = sqrt(6.0);
    verify_solution(1.0/sqrt_6, -2.0/sqrt_6, 1.0/sqrt_6, 1);
    verify_solution(-1.0/sqrt_6, 2.0/sqrt_6, -1.0/sqrt_6, 2);

    printf("\nFiles generated: main.so, main.dat\n");
    printf("Use Python script to read and analyze the data.\n");

    return 0;
}
