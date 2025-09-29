#include <stdio.h>
#include <math.h>

// Function to check if (a-2d) is parallel to (2b-c)
int check_parallel(double a[3], double b[3], double c[3], double d[3]) {
    double u[3], v[3], cross[3];

    // u = a - 2d
    for (int i = 0; i < 3; i++) {
        u[i] = a[i] - 2.0 * d[i];
    }

    // v = 2b - c
    for (int i = 0; i < 3; i++) {
        v[i] = 2.0 * b[i] - c[i];
    }

    // cross product u x v
    cross[0] = u[1]*v[2] - u[2]*v[1];
    cross[1] = u[2]*v[0] - u[0]*v[2];
    cross[2] = u[0]*v[1] - u[1]*v[0];

    // Check if cross product is (almost) zero
    double eps = 1e-9;
    if (fabs(cross[0]) < eps && fabs(cross[1]) < eps && fabs(cross[2]) < eps)
        return 1; // parallel
    else
        return 0; // not parallel
}

