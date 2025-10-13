
#include <stdio.h>

//computing the equation of a plane passing through 2 given vectors and the origin. 

void plane_from_vectors(double a[3], double b[3], double plane[4]) {
    // Cross product n = a × b
    double nx = a[1]*b[2] - a[2]*b[1];
    double ny = a[2]*b[0] - a[0]*b[2];
    double nz = a[0]*b[1] - a[1]*b[0];

    // Plane coefficients are A = nx, B = ny, C = nz, D = 0 (since plane passes through origin)
    plane[0] = nx;
    plane[1] = ny;
    plane[2] = nz;
    plane[3] = 0.0;
}

