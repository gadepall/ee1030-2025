#include <stdio.h>
#include <math.h>

int main() {
    double a, b, x, y;

    // Input parameters
    printf("Enter values of a, b: ");
    scanf("%lf %lf", &a, &b);

    printf("Enter point P(x,y): ");
    scanf("%lf %lf", &x, &y);

    // Define (B - A)
    double BA[2];
    BA[0] = -2 * b;
    BA[1] =  2 * a;

    // Define P
    double P[2];
    P[0] = x;
    P[1] = y;

    // Compute dot product (B - A)^T P
    double dot = BA[0]*P[0] + BA[1]*P[1];

    printf("Matrix form condition:\n");
    printf("(B - A)^T P = %lf\n", dot);

    if (fabs(dot) < 1e-6)
        printf("=> Point lies on locus (bx = ay)\n");
    else
        printf("=> Point does NOT lie on locus\n");

    return 0;
}
