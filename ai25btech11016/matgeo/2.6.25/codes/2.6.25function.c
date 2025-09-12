
#include <math.h>

// Function to compute triangle area using cross product
double triangle_area(double x1, double y1, double x2, double y2, double x3, double y3) {
    // Vectors B-A and C-A
    double ux = x2 - x1;
    double uy = y2 - y1;
    double vx = x3 - x1;
    double vy = y3 - y1;

    // Cross product (2D)
    double cross = ux * vy - uy * vx;

    // Area is half magnitude of cross product
    return 0.5 * fabs(cross);
}
