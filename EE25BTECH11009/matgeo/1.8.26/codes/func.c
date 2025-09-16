#include <stdio.h>

/* Function to compute O on y-axis equidistant from A and B */
void equidistant_yaxis(const double* A, const double* B, double* O) {
    // A = (x1,y1), B = (x2,y2), O = (0,y)
    double x1 = A[0], y1 = A[1];
    double x2 = B[0], y2 = B[1];

    double num = (x1*x1 + y1*y1) - (x2*x2 + y2*y2);
    double den = 2*(y1 - y2);

    O[0] = 0.0;
    O[1] = num/den;
}

/* Generate n points on line AB */
void line_gen(double* X, double* Y, const double* A, const double* B, int n, int m) {
    double temp[2];

    for (int i = 0; i < 2; i++) {
        temp[i] = (B[i] - A[i]) / (double)(n-1);
    }

    for (int i = 0; i < n; i++) {
        X[i] = A[0] + temp[0] * i;
        Y[i] = A[1] + temp[1] * i;
    }
}
