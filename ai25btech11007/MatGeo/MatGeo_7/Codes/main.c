#include <stdio.h>
#include <math.h>

int main() {
    // Angles in degrees
    double alpha = 30.0, beta = 60.0, gamma = 90.0;

    // Direction cosines
    double lx = cos(alpha * M_PI / 180.0);
    double ly = cos(beta * M_PI / 180.0);
    double lz = cos(gamma * M_PI / 180.0);

    printf("Direction cosines:\n");
    printf("cos(30) = %.3f\n", lx);
    printf("cos(60) = %.3f\n", ly);
    printf("cos(90) = %.3f\n", lz);

    // Equation of line through origin: (x/lx) = (y/ly) = (z/lz)
    printf("\nEquation of line:\n");
    printf("y = x / sqrt(3),  z = 0\n");

    // Verify with some values of x
    printf("\nSample points on the line:\n");
    for (int x = 0; x <= 6; x += 2) {
        double y = x / sqrt(3);
        double z = 0;
        printf("(%.2f, %.2f, %.2f)\n", (double)x, y, z);
    }

    return 0;
}
