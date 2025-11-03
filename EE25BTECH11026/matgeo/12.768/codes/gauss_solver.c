#include <stdio.h>

void gauss_solve(double *A, double *b, double *x) {
    double a11 = A[0], a12 = A[1];
    double a21 = A[2], a22 = A[3];
    double b1 = b[0], b2 = b[1];

    if (a11 == 0.0) {
        printf("Mathematical Error: zero pivot\n");
        return;
    }

    // Forward elimination
    double factor = a21 / a11;
    a21 -= factor * a11; // becomes zero
    a22 -= factor * a12;
    b2 -= factor * b1;

    // Back substitution
    if (a22 == 0.0) {
        printf("Mathematical Error: zero pivot in back substitution\n");
        return;
    }

    x[1] = b2 / a22;
    x[0] = (b1 - a12 * x[1]) / a11;
}

