#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Function to calculate rank of a matrix using Gaussian elimination
int calculateRank(double **matrix, int rows, int cols) {
    int rank = 0;
    double epsilon = 1e-10;

    // Make a copy of the matrix to avoid modifying the original
    double **temp = (double**)malloc(rows * sizeof(double*));
    for (int i = 0; i < rows; i++) {
        temp[i] = (double*)malloc(cols * sizeof(double));
        for (int j = 0; j < cols; j++) {
            temp[i][j] = matrix[i][j];
        }
    }

    // Gaussian elimination
    for (int col = 0, row = 0; col < cols && row < rows; col++) {
        // Find pivot
        int pivot = row;
        for (int i = row + 1; i < rows; i++) {
            if (fabs(temp[i][col]) > fabs(temp[pivot][col])) {
                pivot = i;
            }
        }

        if (fabs(temp[pivot][col]) < epsilon) {
            continue;
        }

        // Swap rows if needed
        if (pivot != row) {
            double *temp_row = temp[row];
            temp[row] = temp[pivot];
            temp[pivot] = temp_row;
        }

        // Eliminate column
        for (int i = row + 1; i < rows; i++) {
            if (fabs(temp[i][col]) > epsilon) {
                double factor = temp[i][col] / temp[row][col];
                for (int j = col; j < cols; j++) {
                    temp[i][j] -= factor * temp[row][j];
                }
            }
        }

        row++;
        rank++;
    }

    // Free temporary matrix
    for (int i = 0; i < rows; i++) {
        free(temp[i]);
    }
    free(temp);

    return rank;
}

// Function to analyze the system for different values of p
void analyzeSolution(double p) {
    // Coefficient matrix A = [4, p; 2, 2]
    double **A = (double**)malloc(2 * sizeof(double*));
    for (int i = 0; i < 2; i++) {
        A[i] = (double*)malloc(2 * sizeof(double));
    }

    A[0][0] = 4.0; A[0][1] = p;
    A[1][0] = 2.0; A[1][1] = 2.0;

    // Augmented matrix [A|b] = [4, p, -8; 2, 2, -2]
    double **Ab = (double**)malloc(2 * sizeof(double*));
    for (int i = 0; i < 2; i++) {
        Ab[i] = (double*)malloc(3 * sizeof(double));
    }

    Ab[0][0] = 4.0; Ab[0][1] = p; Ab[0][2] = -8.0;
    Ab[1][0] = 2.0; Ab[1][1] = 2.0; Ab[1][2] = -2.0;

    int rankA = calculateRank(A, 2, 2);
    int rankAb = calculateRank(Ab, 2, 3);

    printf("p = %.2f: rank(A) = %d, rank([A|b]) = %d\n", p, rankA, rankAb);

    if (rankA == rankAb && rankA == 2) {
        printf("  Solution Type: UNIQUE\n");
    } else if (rankA == rankAb && rankA < 2) {
        printf("  Solution Type: INFINITE SOLUTIONS\n");
    } else {
        printf("  Solution Type: NO SOLUTION\n");
    }

    // Free memory
    for (int i = 0; i < 2; i++) {
        free(A[i]);
        free(Ab[i]);
    }
    free(A);
    free(Ab);
}

int main() {
    printf("Analysis of the system of equations:\n");
    printf("4x + py + 8 = 0\n");
    printf("2x + 2y + 2 = 0\n\n");

    // Test various values of p including the critical value p = 4
    double test_values[] = {1.0, 2.0, 3.0, 3.9, 4.0, 4.1, 5.0, 6.0};
    int num_values = sizeof(test_values) / sizeof(test_values[0]);

    FILE *data_file = fopen("main.dat", "w");
    if (!data_file) {
        printf("Error: Could not create main.dat\n");
        return 1;
    }

    fprintf(data_file, "p,rankA,rankAb,solution_type\n");

    for (int i = 0; i < num_values; i++) {
        double p = test_values[i];
        analyzeSolution(p);

        // Calculate ranks for data file
        double **A = (double**)malloc(2 * sizeof(double*));
        double **Ab = (double**)malloc(2 * sizeof(double*));
        for (int j = 0; j < 2; j++) {
            A[j] = (double*)malloc(2 * sizeof(double));
            Ab[j] = (double*)malloc(3 * sizeof(double));
        }

        A[0][0] = 4.0; A[0][1] = p;
        A[1][0] = 2.0; A[1][1] = 2.0;

        Ab[0][0] = 4.0; Ab[0][1] = p; Ab[0][2] = -8.0;
        Ab[1][0] = 2.0; Ab[1][1] = 2.0; Ab[1][2] = -2.0;

        int rankA = calculateRank(A, 2, 2);
        int rankAb = calculateRank(Ab, 2, 3);

        const char* solution_type;
        if (rankA == rankAb && rankA == 2) {
            solution_type = "UNIQUE";
        } else if (rankA == rankAb && rankA < 2) {
            solution_type = "INFINITE";
        } else {
            solution_type = "NO_SOLUTION";
        }

        fprintf(data_file, "%.2f,%d,%d,%s\n", p, rankA, rankAb, solution_type);

        for (int j = 0; j < 2; j++) {
            free(A[j]);
            free(Ab[j]);
        }
        free(A);
        free(Ab);
    }

    fclose(data_file);

    printf("\nConclusion: The system has a unique solution for p ∈ R - {4}\n");
    printf("Data written to main.dat\n");

    return 0;
}
