#include <math.h>

// Function to find the intersection of two lines
// Line 1: a1*x + b1*y = c1
// Line 2: a2*x + b2*y = c2
// result[0] = x, result[1] = y
void intersection(double a1, double b1, double c1,
                  double a2, double b2, double c2,
                  double *result)
{
    double det = a1*b2 - a2*b1;
    if (fabs(det) < 1e-9) {
        // Lines are parallel or coincident
        result[0] = NAN;
        result[1] = NAN;
        return;
    }
    result[0] = (c1*b2 - c2*b1) / det;
    result[1] = (a1*c2 - a2*c1) / det;
}
