#include "solution.h"

int main() {
    double x, y, z;
    double alpha, beta, gamma;

    // Input point Q
    printf("Enter coordinates of Q (x y z): ");
    scanf("%lf %lf %lf", &x, &y, &z);

    // Call reflection function
    reflect_point(x, y, z, &alpha, &beta, &gamma);

    // Output result
    printf("Reflected point S = (%.6lf, %.6lf, %.6lf)\n", alpha, beta, gamma);

    return 0;
}
