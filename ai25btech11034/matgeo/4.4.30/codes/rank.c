#include <stdio.h>
#include <math.h>

#define EPS 1e-9

// Gaussian elimination for 4x4 matrix
int rank4x4(double M[4][4]) {
    int rank = 0;

    for (int col = 0, row = 0; col < 4 && row < 4; col++) {
        // Find pivot
        int pivot = row;
        for (int i = row + 1; i < 4; i++) {
            if (fabs(M[i][col]) > fabs(M[pivot][col]))
                pivot = i;
        }

        // If pivot is zero, skip column
        if (fabs(M[pivot][col]) < EPS)
            continue;

        // Swap rows
        if (pivot != row) {
            for (int j = 0; j < 4; j++) {
                double tmp = M[row][j];
                M[row][j] = M[pivot][j];
                M[pivot][j] = tmp;
            }
        }

        // Normalize pivot row
        double div = M[row][col];
        for (int j = 0; j < 4; j++)
            M[row][j] /= div;

        // Eliminate below
        for (int i = row + 1; i < 4; i++) {
            double factor = M[i][col];
            for (int j = 0; j < 4; j++)
                M[i][j] -= factor * M[row][j];
        }

        row++;
        rank++;
    }

    return rank;
}

// Function to check coplanarity of 4 points
int are_coplanar(double P[4][3]) {
    double M[4][4];

    for (int i = 0; i < 4; i++) {
        M[i][0] = P[i][0];
        M[i][1] = P[i][1];
        M[i][2] = P[i][2];
        M[i][3] = 1.0;
    }

    int r = rank4x4(M);
    return (r <= 3); // 1 if coplanar, 0 otherwise
}

