// distance.c
#include <stdio.h>
#include <math.h>

// Squared norm of a vector
double norm_sq(double v[3]) {
    return v[0]*v[0] + v[1]*v[1] + v[2]*v[2];
}

// Dot product
double dot(double v1[3], double v2[3]) {
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2];
}

// Function to compute distance
double distance_point_line(double p[3], double a[3], double m[3]) {
    double w[3];
    for (int i = 0; i < 3; i++) {
        w[i] = p[i] - a[i];
    }
    double d2 = norm_sq(w) - (dot(m, w) * dot(m, w)) / norm_sq(m);
    return sqrt(d2);
}
