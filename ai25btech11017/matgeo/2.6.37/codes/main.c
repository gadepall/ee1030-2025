#include <stdio.h>
#include <math.h>

int main() {
    // Vectors a and b
    double ax = 2, ay = -3, az = 2;
    double bx = 2, by = 3,  bz = 1;

    // Cross product a × b
    double cx = ay*bz - az*by;
    double cy = az*bx - ax*bz;
    double cz = ax*by - ay*bx;

    // Magnitude of cross product
    double magnitude = sqrt(cx*cx + cy*cy + cz*cz);

    // Area of triangle OAB
    double area = 0.5 * magnitude;

    printf("The area of triangle OAB is: %.2f\n", area);

    return 0;
}