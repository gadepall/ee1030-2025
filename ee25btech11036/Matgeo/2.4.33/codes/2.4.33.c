#include <stdio.h>
#include <math.h>

// Function to compute squared distance using matrices
double dist2(double P[2], double Q[2]) {
    double diff[2];
    diff[0] = P[0] - Q[0];
    diff[1] = P[1] - Q[1];
    return diff[0]*diff[0] + diff[1]*diff[1];
}

int main() {
    double A[2] = {-5, 6};
    double B[2] = {-4, -2};
    double C[2] = {7, 5};

    // Distances squared
    double AB2 = dist2(A, B);
    double BC2 = dist2(B, C);
    double CA2 = dist2(C, A);

    printf("AB^2 = %.2lf, BC^2 = %.2lf, CA^2 = %.2lf\n", AB2, BC2, CA2);

    // Check for type
    if (fabs(AB2 - BC2) < 1e-6 || fabs(BC2 - CA2) < 1e-6 || fabs(CA2 - AB2) < 1e-6)
        printf("The triangle is Isosceles.\n");
    else
        printf("The triangle is Scalene.\n");

    if (fabs(AB2 + BC2 - CA2) < 1e-6 || fabs(BC2 + CA2 - AB2) < 1e-6 || fabs(CA2 + AB2 - BC2) < 1e-6)
        printf("It is also a Right-angled triangle.\n");

    return 0;
}
