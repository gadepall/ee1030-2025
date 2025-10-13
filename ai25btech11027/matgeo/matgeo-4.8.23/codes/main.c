#include <math.h>

//distance from point (x, y, z) to plane 3x + 5y + 4z = 11
double point_to_plane_distance(double x, double y, double z) {
    double numerator = fabs(3.0 * x + 5.0 * y + 4.0 * z - 11.0);
    double denominator = sqrt(3.0 * 3.0 + 5.0 * 5.0 + 4.0 * 4.0);  // sqrt(50)
    return numerator / denominator;
}

