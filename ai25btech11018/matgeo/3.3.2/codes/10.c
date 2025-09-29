#include <stdio.h>
#include <math.h>

int main() {
    // Side lengths
    double AB = 5.0; // between A and B
    double BC = 6.0; // between B and C
    double CA = 7.0; // between C and A

    // Coordinates of points
    double Ax = 0.0, Ay = 0.0;
    double Bx = AB, By = 0.0;

    // Calculate cosA using the law of cosines
    double cosA = (AB*AB + CA*CA - BC*BC) / (2 * AB * CA);

    // Calculate sinA using identity sin^2 A + cos^2 A = 1
    double sinA = sqrt(1 - cosA*cosA);

    // Coordinates of C
    double Cx = CA * cosA;
    double Cy = CA * sinA;

    printf("Coordinates of A: (%.2f, %.2f)\n", Ax, Ay);
    printf("Coordinates of B: (%.2f, %.2f)\n", Bx, By);
    printf("Coordinates of C: (%.2f, %.2f)\n", Cx, Cy);

    return 0;
}

