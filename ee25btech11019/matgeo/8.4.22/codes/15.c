#include <stdio.h>
#include <math.h>

// Function to find circle radius
float circle_radius() {
    // Ellipse: x^2/16 + y^2/9 = 1
    float a2 = 16.0;   // a^2
    float b2 = 9.0;    // b^2

    // Focal distance from origin: c = sqrt(a^2 - b^2)
    float c = sqrt(a2 - b2); // sqrt(7)

    // Foci: (±sqrt(7), 0)
    // Centre of circle: (0, 3)
    // Radius = distance between (sqrt(7), 0) and (0, 3)
    float radius = sqrt((c - 0)*(c - 0) + (0 - 3)*(0 - 3));

    return radius; // should be 4
}
