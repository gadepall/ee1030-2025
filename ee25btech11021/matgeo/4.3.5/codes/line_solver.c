#include <stdio.h>
#include <math.h>

// Function: line through A at 30° with y-axis
// Inputs: Ax, Ay
// Outputs: nx, ny, c in n^T x = c
void line_equation(double Ax, double Ay, double *nx, double *ny, double *c) {
    double angle = 30.0 * M_PI / 180.0;
    double m = 1.0 / tan(angle);   // slope
    *nx = m;       // √3
    *ny = -1.0;
    *c  = (*nx)*Ax + (*ny)*Ay;   // n^T A
}

