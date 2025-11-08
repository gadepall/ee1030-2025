#include <stdio.h>

void matrix_inverse(double input[3][3], double output[3][3]) {
    // Calculate determinant
    double det = input[0][0] * (input[1][1] * input[2][2] - input[1][2] * input[2][1]) -
                 input[0][1] * (input[1][0] * input[2][2] - input[1][2] * input[2][0]) +
                 input[0][2] * (input[1][0] * input[2][1] - input[1][1] * input[2][0]);

    // Calculate matrix of minors
    double minors[3][3];
    minors[0][0] = input[1][1] * input[2][2] - input[1][2] * input[2][1];
    minors[0][1] = -(input[1][0] * input[2][2] - input[1][2] * input[2][0]);
    minors[0][2] = input[1][0] * input[2][1] - input[1][1] * input[2][0];
    minors[1][0] = -(input[0][1] * input[2][2] - input[0][2] * input[2][1]);
    minors[1][1] = input[0][0] * input[2][2] - input[0][2] * input[2][0];
    minors[1][2] = -(input[0][0] * input[2][1] - input[0][1] * input[2][0]);
    minors[2][0] = input[0][1] * input[1][2] - input[0][2] * input[1][1];
    minors[2][1] = -(input[0][0] * input[1][2] - input[0][2] * input[1][0]);
    minors[2][2] = input[0][0] * input[1][1] - input[0][1] * input[1][0];

    // Transpose of matrix of minors (adjoint)
    double adjoint[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            adjoint[i][j] = minors[j][i];
        }
    }

    // Compute inverse: (1/det) * adjoint
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            output[i][j] = adjoint[i][j] / det;
        }
    }
}
