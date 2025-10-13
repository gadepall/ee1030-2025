#include <stdio.h>

// Function to find intersection point of two lines
// Equation 1: a1*x + b1*y = c1
// Equation 2: a2*x + b2*y = c2
void findIntersection(double a1, double b1, double c1,
                      double a2, double b2, double c2,
                      double *x, double *y)
{
    double det = a1 * b2 - a2 * b1;

    if (det == 0) {
        // Lines are parallel or coincident
        *x = *y = 0;
        printf("Lines are parallel, no intersection.\n");
    } else {
        *x = (c1 * b2 - c2 * b1) / det;
        *y = (a1 * c2 - a2 * c1) / det;
    }
}