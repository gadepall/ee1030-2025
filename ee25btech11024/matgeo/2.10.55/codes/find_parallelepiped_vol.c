#include <stdio.h>
#include <math.h>

// Function to compute determinant of 3x3 matrix
double determinant3x3(double m[3][3]) {
    return m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
         - m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
         + m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]);
}

// C function: takes 3 vectors (a,b,c), returns parallelepiped volume
double parallelepiped_volume(double *a, double *b, double *c) {
    double m[3][3] = {
        {a[0], b[0], c[0]},
        {a[1], b[1], c[1]},
        {a[2], b[2], c[2]}
    };
    double det = determinant3x3(m);
    return fabs(det); // absolute value = volume
}
