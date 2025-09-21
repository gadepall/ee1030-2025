#include <math.h>
#include "triangle.h"

void cross_product(const double a[3], const double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

double magnitude(const double v[3]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

double triangle_area(const double OA[3], const double OB[3]) {
    double cross[3];
    cross_product(OA, OB, cross);
    return 0.5 * magnitude(cross);
}

