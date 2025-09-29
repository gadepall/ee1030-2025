#include <stdio.h>
#include "solution.h"

int main() {
    double a[3], b[3], c[3], k;

    // Input
    printf("Enter vector a (3 values): ");
    scanf("%lf %lf %lf", &a[0], &a[1], &a[2]);

    printf("Enter vector b (3 values): ");
    scanf("%lf %lf %lf", &b[0], &b[1], &b[2]);

    printf("Enter scalar k (a·c): ");
    scanf("%lf", &k);

    // Compute c
    compute_c(a, b, k, c);

    // Output
    printf("\nVector c = (%.2lf, %.2lf, %.2lf)\n", c[0], c[1], c[2]);

    return 0;
}

