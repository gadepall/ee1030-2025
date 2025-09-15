#include <stdio.h>
#include <math.h>

int main(void) {
    /* Planes:
       Plane 1: 2x - 3y + 6z - 4 = 0    => a=2, b=-3, c=6, d1 = -4
       Plane 2: 6x - 9y + 18z + 30 = 0  => divide by 3:
                2x - 3y + 6z + 10 = 0  => d2 = 10
    */

    double a = 2.0, b = -3.0, c = 6.0;
    double d1 = -4.0, d2 = 10.0;

    double numerator = fabs(d2 - d1);              // |10 - (-4)| = 14
    double denominator = sqrt(a*a + b*b + c*c);    // sqrt(4 + 9 + 36) = sqrt(49) = 7
    double distance = numerator / denominator;     // 14 / 7 = 2

    printf("Numerator |d2 - d1| = %.0f\n", numerator);
    printf("Denominator ||n|| = sqrt(a^2+b^2+c^2) = %.0f\n", denominator);
    printf("Distance between the planes = %.0f\n", distance);

    return 0;
}
