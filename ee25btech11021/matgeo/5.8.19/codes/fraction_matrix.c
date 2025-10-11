#include <stdio.h>

// Generate augmented matrix for fraction problem
void generate_matrix(double matrix[2][3]) {
    // Equation 1: x - y = -2
    matrix[0][0] = 1;
    matrix[0][1] = -1;
    matrix[0][2] = -2;

    // Equation 2: 2x - y = 1
    matrix[1][0] = 2;
    matrix[1][1] = -1;
    matrix[1][2] = 1;
}


