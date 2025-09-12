#include <math.h>

// Returns 1 if 3x=2y within tolerance, else 0
int equidist_check(double x, double y, double tol) {
    double val = 3.0*x - 2.0*y;
    return fabs(val) <= tol ? 1 : 0;
}
