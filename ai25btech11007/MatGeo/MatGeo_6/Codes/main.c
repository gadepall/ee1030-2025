#include <stdio.h>
#include <math.h>

// Custom sqrt (overrides math.h sqrt)
double sqrt(double n) {
    if (n < 0) return -1; // invalid for negative numbers
    if (n == 0) return 0;

    double guess = n / 2.0;
    for (int i = 0; i < 20; i++) { // Newton-Raphson iterations
        guess = 0.5 * (guess + n / guess);
    }
    return guess;
}

// Function to calculate dot product of two vectors
double dotProduct(double A[], double B[]) {
    return A[0]*B[0] + A[1]*B[1];
}

// Function to calculate magnitude of a vector
double magnitude(double V[]) {
    return sqrt(V[0]*V[0] + V[1]*V[1]);
}

#include <stdio.h>
#include <math.h>

int main(void) {
    /* Given data */
    double a = 5.0;       /* BC */
    double K = 7.5;       /* AC + AB = b + c */
    double cosB = 0.5;    /* cos 60° */
    double sinB = sqrt(3.0) / 2.0; /* sin 60° */

    /* Formula from your solution */
    double c = (K*K - a*a) / (2.0 * (K - a * cosB));
    double b = K - c;

    /* Coordinates with B=(0,0), C=(a,0) */
    double Ax = (c * cosB) / sinB;
    double Ay = c / sinB;

    printf("Computed values:\n");
    printf("c (AC) = %.6f\n", c);
    printf("b (AB) = %.6f\n", b);
    printf("A = (%.6f, %.6f)\n", Ax, Ay);
    printf("B = (0.000000, 0.000000)\n");
    printf("C = (%.6f, 0.000000)\n", a);

    return 0;
}
