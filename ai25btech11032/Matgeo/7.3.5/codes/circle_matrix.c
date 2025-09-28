#include <math.h>

// Circle through (0,0), (a,0), (0,b) using direct expansion of matrix equations
void circle_center_matrix(double a, double b,
                          double *cx, double *cy, double *r)
{
    // From equations:
    // f = 0
    // 2a u1 + f = -a^2  -> u1 = -a/2
    // 2b u2 + f = -b^2  -> u2 = -b/2
    double u1 = -a/2.0;
    double u2 = -b/2.0;

    *cx = -u1;   // = a/2
    *cy = -u2;   // = b/2

    if (r) {
        *r = sqrt((*cx)*(*cx) + (*cy)*(*cy));
    }
}

