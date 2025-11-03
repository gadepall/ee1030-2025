#include "solution.h"

int main() {
    Point A, C, D;

    // Input A, C, D
    printf("Enter coordinates of A (x y z): ");
    scanf("%lf %lf %lf", &A.x, &A.y, &A.z);

    printf("Enter coordinates of C (x y z): ");
    scanf("%lf %lf %lf", &C.x, &C.y, &C.z);

    printf("Enter coordinates of D (x y z): ");
    scanf("%lf %lf %lf", &D.x, &D.y, &D.z);

    // Solve for x
    double x = solve_for_x(A, C, D);

    printf("The value of x such that A, B, C, D are coplanar is: %.2f\n", x);

    return 0;
}

