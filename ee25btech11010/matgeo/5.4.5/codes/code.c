#include <stdio.h>

int inverse2x2(double A[2][2], double inv[2][2]) {
    double a = A[0][0], b = A[0][1];
    double c = A[1][0], d = A[1][1];
    double det = a*d - b*c;

    if (det == 0) {
        printf("Matrix is singular, inverse doesn't exist.\n");
        return 0;
    }

    inv[0][0] =  d / det;
    inv[0][1] = -b / det;
    inv[1][0] = -c / det;
    inv[1][1] =  a / det;

    return 1;
}