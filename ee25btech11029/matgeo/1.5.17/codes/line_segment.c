#include <stdio.h>

void line_segment_gen(double *X, double *Y, double *A, double *B, int n)
{
    double dx = (B[0] - A[0]) / (double)n;
    double dy = (B[1] - A[1]) / (double)n;

    for (int i = 0; i <= n; i++)
    {
        X[i] = A[0] + dx * i;
        Y[i] = A[1] + dy * i;
    }
}
