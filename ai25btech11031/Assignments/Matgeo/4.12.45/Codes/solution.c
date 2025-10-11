#include <stdio.h>
#include <math.h>
#include "solution.h"

int main() {
    double A[3], B[3];
    double constant_sum;
    double a2, b2, c2;

    printf("Enter coordinates of point A (Ax Ay Az): ");
    scanf("%lf %lf %lf", &A[0], &A[1], &A[2]);

    printf("Enter coordinates of point B (Bx By Bz): ");
    scanf("%lf %lf %lf", &B[0], &B[1], &B[2]);

    printf("Enter the constant sum of distances: ");
    scanf("%lf", &constant_sum);

    standard_form(A, B, constant_sum, &a2, &b2, &c2);

    printf("\nStandard form of the locus equation:\n");
    printf("x^2/(%.6lf) + y^2/(%.6lf) + z^2/(%.6lf) = 1\n", a2, b2, c2);

    printf("\nWhere:\n");
    printf("a = %.6lf, b = %.6lf, c = %.6lf\n", sqrt(a2), sqrt(b2), sqrt(c2));

    return 0;
}

