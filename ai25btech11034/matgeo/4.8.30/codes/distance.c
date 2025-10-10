// distance.c
#include <math.h>

double shortest_distance(double p1[3], double p2[3], double v[3]) {
    double w[3];
    w[0] = p2[0] - p1[0];
    w[1] = p2[1] - p1[1];
    w[2] = p2[2] - p1[2];

    // cross product w x v
    double cx = w[1]*v[2] - w[2]*v[1];
    double cy = w[2]*v[0] - w[0]*v[2];
    double cz = w[0]*v[1] - w[1]*v[0];

    double num = sqrt(cx*cx + cy*cy + cz*cz);
    double den = sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
    return num / den;
}

