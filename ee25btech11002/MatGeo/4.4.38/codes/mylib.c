#include <stdio.h>
void midpoint(double *A, double *B, double *h, int n)
{
    for(int i=0; i<n; i++)
    {
        h[i] = (A[i] + B[i]) / 2;
    }
}

void cross_product(double *m1, double *m2, double *m)
{
    m[0] = m1[1]*m2[2] - m1[2]*m2[1];
    m[1] = m1[2]*m2[0] - m1[0]*m2[2];
    m[2] = m1[0]*m2[1] - m1[1]*m2[0];
}

void compute_line(double *x, double *y, double *z, double *h, double *m, int n)
{
    for(int i=0; i<n; i++)
    {
        double k = (i - n/2);
        x[i] = h[0] + k*m[0];
        y[i] = h[1] + k*m[1];
        z[i] = h[2] + k*m[2];
    }
}
