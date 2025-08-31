#include "func.h"

// Function to check collinearity
int check_collinear(double a, double b, double c) {
    double mat[2][2];

    // Matrix [[b-a, c-a], [a-b, a-c]]
    mat[0][0] = b - a;
    mat[0][1] = c - a;
    mat[1][0] = a - b;
    mat[1][1] = a - c;

    // Determinant
    double det = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0];

    return (det == 0);  // 1 if collinear, 0 otherwise
}

