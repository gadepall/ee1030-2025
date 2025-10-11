#include <stdio.h>

double calculate_trace(double matrix[3][3]) {
    return matrix[0][0] + matrix[1][1] + matrix[2][2];
}

double calculate_determinant(double matrix[3][3]) {
    double det = 0;

    det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
          matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
          matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);

    return det;
}
