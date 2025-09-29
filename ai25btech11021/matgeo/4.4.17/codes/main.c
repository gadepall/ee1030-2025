#include <stdio.h>

void calculateP(double A[2], double B[2], double K, double P[2]) {
    P[0] = (K * B[0] + A[0]) / (K + 1);
    P[1] = (K * B[1] + A[1]) / (K + 1);
}

int main() {
    double A[2] = {3, -5};
    double B[2] = {-4, 8};
    double K = 0.5;  // example value for K
    double P[2];

    calculateP(A, B, K, P);

    printf("Coordinates of P are: (%.2f, %.2f)\n", P[0], P[1]);

    return 0;
}
