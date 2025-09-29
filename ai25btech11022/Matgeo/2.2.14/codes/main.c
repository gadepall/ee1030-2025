#include <stdio.h>
#include <math.h>

// Function to compute dot product of 3D vectors
double dot(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Function to compute norm (magnitude) of vector
double norm(double a[3]) {
    return sqrt(dot(a, a));
}

// Function to compute angle between line and plane (in degrees)
double angle_line_plane(double d[3], double n[3]) {
    double cos_theta = fabs(dot(d, n)) / (norm(d) * norm(n));
    double theta = asin(cos_theta);  // radians
    return theta * (180.0 / M_PI);   // convert to degrees
}

