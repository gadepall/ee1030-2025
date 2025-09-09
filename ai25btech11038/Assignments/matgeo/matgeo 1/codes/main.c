// main.c
#include <stdio.h>

// Declare external function
void find_ratio(double P[3], double Q[3], double R[3], double *m, double *n);

int main() {
    double P[3] = {3, 2, -4};
    double Q[3] = {5, 4, -6};
    double R[3] = {9, 8, -10};
    double m, n;

    find_ratio(P, Q, R, &m, &n);

    printf("Q divides PR in the ratio %.2f : %.2f\n", m, n);

    return 0;
}