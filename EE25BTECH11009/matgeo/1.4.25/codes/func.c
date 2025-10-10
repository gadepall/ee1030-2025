void section(double* P, double* Q, double* R, int m) {
    for (int i = 0; i < m; i++) {
        R[i] = (Q[i] - 2 * P[i]) / (1 - 2);
    }
}

void line_gen(double* X, double* Y, const double* A, const double* B, int n, int m) {
    double temp[2];

    /* Step size per coordinate */
    for (int i = 0; i < 2; i++) {
        temp[i] = (B[i] - A[i]) / (double)n;
    }

    /* Parametric points from A to B */
    for (int i = 0; i <= n; i++) {
        X[i] = A[0] + temp[0] * i;
        Y[i] = A[1] + temp[1] * i;
    }
}
