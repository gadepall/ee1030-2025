#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

#define N 3

void printMatrix(double mat[N][N], const char* name);
void multiplyMatrices(double mat1[N][N], double mat2[N][N], double result[N][N]);
bool invertMatrix(double mat[N][N], double inverse[N][N]);
void scalarMultiply(double scalar, double mat[N][N], double result[N][N]);
void subtractMatrices(double mat1[N][N], double mat2[N][N], double result[N][N]);

int main() {
    double A[N][N] = {
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 1.0},
        {0.0, -2.0, 4.0}
    };

    double A_squared[N][N];
    double A_inverse[N][N];
    double temp_matrix[N][N];
    double RHS_matrix[N][N];

    printf("--- Initial Matrix A ---\n");
    printMatrix(A, "A");

    multiplyMatrices(A, A, A_squared);
    printf("\n--- Step 1: Calculated A^2 ---\n");
    printMatrix(A_squared, "A^2");

    printf("\n--- Step 2: Calculating A^-1 ---\n");
    if (!invertMatrix(A, A_inverse)) {
        printf("Matrix A is not invertible. Cannot solve.\n");
        return 1;
    }
    printMatrix(A_inverse, "A^-1");

    printf("\n--- Step 3: Calculating RHS = 6*A^-1 - A^2 ---\n");
    scalarMultiply(6.0, A_inverse, temp_matrix);
    printMatrix(temp_matrix, "6 * A^-1");

    subtractMatrices(temp_matrix, A_squared, RHS_matrix);
    printMatrix(RHS_matrix, "RHS Matrix");

    double c = RHS_matrix[1][2];
    double d = RHS_matrix[1][1] - c;

    printf("\n--- Step 4: Solved for c and d ---\n");
    printf("From element (2, 3) of the matrix equation, we get c = %.2f\n", c);
    printf("From element (2, 2), we get c + d = %.2f, so d = %.2f - %.2f = %.2f\n", RHS_matrix[1][1], RHS_matrix[1][1], c, d);

    printf("\n====================================\n");
    printf("           Final Solution           \n");
    printf("====================================\n");
    printf("c = %.2f\n", c);
    printf("d = %.2f\n", d);
    printf("====================================\n");

    return 0;
}

void printMatrix(double mat[N][N], const char* name) {
    printf("Matrix %s:\n", name);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%8.3f ", mat[i][j]);
        }
        printf("\n");
    }
}

void multiplyMatrices(double mat1[N][N], double mat2[N][N], double result[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result[i][j] = 0;
            for (int k = 0; k < N; k++) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
}

bool invertMatrix(double mat[N][N], double inverse[N][N]) {
    double augvec[N][N * 2];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            augvec[i][j] = mat[i][j];
        }
        for (int j = 0; j < N; j++) {
            augvec[i][j + N] = (i == j) ? 1.0 : 0.0;
        }
    }

    for (int i = 0; i < N; i++) {
        double pivot = augvec[i][i];

        if (pivot == 0) {
            int max_row = i;
            for (int k = i + 1; k < N; k++) {
                if (fabs(augvec[k][i]) > fabs(augvec[max_row][i])) {
                    max_row = k;
                }
            }

            if (max_row != i) {
                for (int j = 0; j < 2 * N; j++) {
                    double temp = augvec[i][j];
                    augvec[i][j] = augvec[max_row][j];
                    augvec[max_row][j] = temp;
                }
            }
        }
        
        pivot = augvec[i][i];

        if (pivot == 0) return false;

        for (int j = 0; j < 2 * N; j++) {
            augvec[i][j] /= pivot;
        }

        for (int k = 0; k < N; k++) {
            if (k != i) {
                double factor = augvec[k][i];
                for (int j = 0; j < 2 * N; j++) {
                    augvec[k][j] -= factor * augvec[i][j];
                }
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            inverse[i][j] = augvec[i][j + N];
        }
    }
    return true;
}

void scalarMultiply(double scalar, double mat[N][N], double result[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result[i][j] = mat[i][j] * scalar;
        }
    }
}

void subtractMatrices(double mat1[N][N], double mat2[N][N], double result[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result[i][j] = mat1[i][j] - mat2[i][j];
        }
    }
}

