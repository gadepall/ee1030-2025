#include <math.h>

double determinant(int n, double matrix[n][n]) {
    if (n == 1)
        return matrix[0][0];

    double det = 0.0;
    double submatrix[n-1][n-1];

    for (int col = 0; col < n; col++) {
        // Create submatrix excluding row 0 and current column
        int subi = 0;
        for (int i = 1; i < n; i++) {
            int subj = 0;
            for (int j = 0; j < n; j++) {
                if (j == col)
                    continue;
                submatrix[subi][subj] = matrix[i][j];
                subj++;
            }
            subi++;
        }

        // Apply cofactor expansion with (-1)^(row+col)
        double sign = pow(-1, 0 + col);
        det += sign * matrix[0][col] * determinant(n - 1, submatrix);
    }

    return det;
}

