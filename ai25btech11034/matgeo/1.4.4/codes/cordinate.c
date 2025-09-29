#include <stdio.h>

int main() {
    // Define input vectors P and Q
    double P[2] = {4, 3};
    double Q[2] = {8, 5};
    double R[2];

    // Ratio m:n = 3:1
    double m = 3, n = 1;

    // Section formula: R = (n*P + m*Q) / (m+n)
    R[0] = (n*P[0] + m*Q[0]) / (m + n);
    R[1] = (n*P[1] + m*Q[1]) / (m + n);

    // Output
    printf("Point P = (%.2f, %.2f)\n", P[0], P[1]);
    printf("Point Q = (%.2f, %.2f)\n", Q[0], Q[1]);
    printf("Point R dividing PQ in ratio %.0f:%.0f = (%.2f, %.2f)\n",
           m, n, R[0], R[1]);

    return 0;
}

