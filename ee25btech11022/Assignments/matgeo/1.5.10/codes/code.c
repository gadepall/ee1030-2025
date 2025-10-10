#include <stdio.h>

void division_point(double *A, double *B, double *P, double *k) {
    *k = -A[1] / B[1];
    P[0] = ((*k) * B[0] + A[0]) / ((*k) + 1);
    P[1] = 0;
}

int main() {
    double A[2] = {1, -5};
    double B[2] = {-4, 5};
    double P[2];
    double k;
    division_point(A, B, P, &k);
    printf("Ratio: %f : 1\n", k);
    printf("Division Point: (%f, %f)\n", P[0], P[1]);
    return 0;
}

