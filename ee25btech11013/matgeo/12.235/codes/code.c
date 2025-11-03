#include <stdio.h>

void solve_planes(double *A, double *b, double *x) {
    double detA, det1, det2, det3;

    detA = A[0]*(A[4]*A[8] - A[5]*A[7]) -
           A[1]*(A[3]*A[8] - A[5]*A[6]) +
           A[2]*(A[3]*A[7] - A[4]*A[6]);

    if(detA == 0) {
        x[0] = x[1] = x[2] = 0;
        return;
    }

    det1 = b[0]*(A[4]*A[8] - A[5]*A[7]) -
           A[1]*(b[1]*A[8] - A[5]*b[2]) +
           A[2]*(b[1]*A[7] - A[4]*b[2]);

    det2 = A[0]*(b[1]*A[8] - A[5]*b[2]) -
           b[0]*(A[3]*A[8] - A[5]*A[6]) +
           A[2]*(A[3]*b[2] - b[1]*A[6]);

    det3 = A[0]*(A[4]*b[2] - b[1]*A[7]) -
           A[1]*(A[3]*b[2] - b[1]*A[6]) +
           b[0]*(A[3]*A[7] - A[4]*A[6]);

    x[0] = det1 / detA;
    x[1] = det2 / detA;
    x[2] = det3 / detA;
}
