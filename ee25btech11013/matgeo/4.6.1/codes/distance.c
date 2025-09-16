
#include <math.h>


double norm(double *n) {
    return sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);
}


double plane_distance(double *n, double a, double b) {
    double num = fabs(a - b);
    double denom = norm(n);
    return num / denom;
}
