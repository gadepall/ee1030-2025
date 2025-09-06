#include <stdio.h>
#include <math.h>

#define ROWS 3
#define COLS 2

// Function to find rank of a matrix using row echelon form
int rankMatrix(double mat[ROWS][COLS]) {
    int rank = COLS;
    int row, col;

    for (row = 0, col = 0; row < ROWS && col < rank; col++) {
        // Find pivot
        int pivot = row;
        for (int i = row + 1; i < ROWS; i++) {
            if (fabs(mat[i][col]) > fabs(mat[pivot][col])) {
                pivot = i;
            }
        }

        // If pivot is zero, reduce rank
        if (fabs(mat[pivot][col]) < 1e-8) {
            for (int i = 0; i < ROWS; i++) {
                mat[i][col] = mat[i][rank - 1];
            }
            rank--;
            col--;
            continue;
        }

        // Swap rows
        if (pivot != row) {
            for (int j = 0; j < rank; j++) {
                double temp = mat[row][j];
                mat[row][j] = mat[pivot][j];
                mat[pivot][j] = temp;
            }
        }

        // Make lower elements zero
        for (int i = row + 1; i < ROWS; i++) {
            double factor = mat[i][col] / mat[row][col];
            for (int j = col; j < rank; j++) {
                mat[i][j] -= factor * mat[row][j];
            }
        }
        row++;
    }

    return rank;
}

int main() {
    double M[ROWS][COLS] = {
        {-3, -2},
        {5, 10.0/3.0},
        {-3, -2}
    };

    int r = rankMatrix(M);

    printf("Rank of the matrix = %d\n", r);

    return 0;
}
