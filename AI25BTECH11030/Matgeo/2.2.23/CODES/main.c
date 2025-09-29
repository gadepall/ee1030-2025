// main.c
#include <stdio.h>
#include <math.h>
#include "VectorLib.h"

int main() {
    Vector3D a = createVector(1, 1, -1);    // vector a = i + j - k
    Vector3D b = createVector(1, -1, 1);    // vector b = i - j + k

    double theta = angleBetween(a, b);  // radians

    printf("Angle between vectors a and b is %.6f radians\n", theta);
    printf("Angle between vectors a and b is %.6f degrees\n", theta * (180.0 / M_PI));

    return 0;
}
