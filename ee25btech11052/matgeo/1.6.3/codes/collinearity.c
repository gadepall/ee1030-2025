#include <math.h>

// Return 1 if collinear, 0 otherwise
int check_collinearity(double x1, double y1,
                       double x2, double y2,
                       double x3, double y3,
                       double tol)
{
    double det = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
    return fabs(det) <= tol ? 1 : 0;
}
