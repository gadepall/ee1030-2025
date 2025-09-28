#include <stdio.h>
#include <math.h>

int main() {
    // Circle centre
    double h = 1, k = -2;

    // Solve intersection of 3x + y = 14  and  2x + 5y = 18
    // Equation 1: 3x + y = 14  --> y = 14 - 3x
    // Substitute in 2x + 5y = 18
    double x, y;
    x = (18 - 5*14) / (2 - 15);   // Simplified from substitution
    y = 14 - 3*x;

    // Radius = distance between (h,k) and intersection point
    double r = sqrt(pow(x - h, 2) + pow(y - k, 2));

    // Print results
    printf("Intersection Point: (%.2f, %.2f)\n", x, y);
    printf("Centre: (%.2f, %.2f)\n", h, k);
    printf("Radius: %.2f\n", r);
    printf("Equation of Circle: (x - %.2f)^2 + (y - %.2f)^2 = %.2f^2\n", h, k, r);

    return 0;
}
