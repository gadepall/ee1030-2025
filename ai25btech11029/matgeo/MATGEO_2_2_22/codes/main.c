#include <stdio.h>
#include <math.h>
#include "vector_angle.h"

int main() {
    Vector a = {1.0, 0.0, 0.0};
    Vector b = {1.0, sqrt(3.0), 0.0};

    double angle_rad = angle_between(a, b);
    double angle_deg = angle_rad * (180.0 / M_PI);

    printf("Angle between vectors: %.2f degrees\n", angle_deg);
    return 0;
}
