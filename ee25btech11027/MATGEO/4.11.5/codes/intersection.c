#include <stdio.h>

void solve(double *out) {
    int A[3] = {2, 5, -3};
    int B[3] = {-2, -3, 5};
    int C[3] = {5, 3, -3};
    int P[3] = {3, 1, 5};
    int Q[3] = {-1, -3, -1};

    // vectors
    int AB[3] = {B[0]-A[0], B[1]-A[1], B[2]-A[2]};
    int AC[3] = {C[0]-A[0], C[1]-A[1], C[2]-A[2]};

    // normal = AB x AC
    int n[3];
    n[0] = AB[1]*AC[2] - AB[2]*AC[1];
    n[1] = AB[2]*AC[0] - AB[0]*AC[2];
    n[2] = AB[0]*AC[1] - AB[1]*AC[0];
    int d = -(n[0]*A[0] + n[1]*A[1] + n[2]*A[2]);

    // direction of PQ
    int v[3] = {Q[0]-P[0], Q[1]-P[1], Q[2]-P[2]};
    int num = -(n[0]*P[0] + n[1]*P[1] + n[2]*P[2] + d);
    int den = n[0]*v[0] + n[1]*v[1] + n[2]*v[2];

    double t = (double)num / den;
    double X = P[0] + t*v[0];
    double Y = P[1] + t*v[1];
    double Z = P[2] + t*v[2];

    // output: n0, n1, n2, d, X, Y, Z
    out[0] = n[0];
    out[1] = n[1];
    out[2] = n[2];
    out[3] = d;
    out[4] = X;
    out[5] = Y;
    out[6] = Z;
}
