#include <stdio.h>
#include <math.h>

// Function to compute area of a triangle given coordinates
double triangle_area(double *A, double *B, double *C) {
    // A, B, C are arrays of size 2: [x, y]
    double x1 = A[0], y1 = A[1];
    double x2 = B[0], y2 = B[1];
    double x3 = C[0], y3 = C[1];

    // Determinant method for area
    double det = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2);
    return fabs(det) / 2.0;
}

/* Build as shared library:
   gcc -fPIC -shared -o func.so func.c
*/
