#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("matrix.dat", "w");  // open file for writing
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Define the given matrices
    int A[2][2] = { {5, 2}, {0, 9} };  // X + Y
    int B[2][2] = { {3, 6}, {0, -1} }; // X - Y
    int X[2][2], Y[2][2];

    // Calculate X = (A + B)/2
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            X[i][j] = (A[i][j] + B[i][j]) / 2;
        }
    }

    // Calculate Y = (A - B)/2
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            Y[i][j] = (A[i][j] - B[i][j]) / 2;
        }
    }

    // Write results to file
    fprintf(fp, "Matrix X:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            fprintf(fp, "%d ", X[i][j]);
        }
        fprintf(fp, "\n");
    }

    fprintf(fp, "\nMatrix Y:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            fprintf(fp, "%d ", Y[i][j]);
        }
        fprintf(fp, "\n");
    }

    fclose(fp);
    printf("Solution written to matrix.dat\n");
    return 0;
}

