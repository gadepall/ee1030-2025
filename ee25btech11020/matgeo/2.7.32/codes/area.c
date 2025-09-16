#include <stdio.h>
#include <math.h>

double triangle_area(double p1[2], double p2[2], double p3[2]) {
    double area = 0.5 * fabs(
        p1[0]*(p2[1] - p3[1]) +
        p2[0]*(p3[1] - p1[1]) +
        p3[0]*(p1[1] - p2[1])
    );
    return area;
}
