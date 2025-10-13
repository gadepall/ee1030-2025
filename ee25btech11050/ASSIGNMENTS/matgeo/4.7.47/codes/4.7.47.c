#include <stdio.h>

/* Solve 2x2 system:
   [a00 a01] [x] = [b0]
   [a10 a11] [y]   [b1]
   Returns solution in rx, ry (pointers).
*/
void solve_system(double a00, double a01,
                  double a10, double a11,
                  double b0,  double b1,
                  double *rx,   double *ry)
{
    double det = a00 * a11 - a01 * a10;
    if (det == 0.0) {
        /* Singular matrix -- not expected here */
        *rx = 0.0;
        *ry = 0.0;
        return;
    }
    *rx = (b0 * a11 - b1 * a01) / det;
    *ry = (a00 * b1 - a10 * b0) / det;
}

