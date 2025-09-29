#include <stdio.h>

/*
 * Compute AP and PB (vertical distances) and x-coordinate of P (using section formula).
 *
 * Inputs:
 *   Ax, Ay, Bx, By, yP
 *
 * Outputs (via pointers):
 *   *ratio_AP : AP (vertical distance Ay - yP)
 *   *ratio_PB : PB (vertical distance yP - By)
 *   *xP       : x-coordinate of P computed by section formula
 */
void section_point(double Ax, double Ay, double Bx, double By, double yP,
                   double *ratio_AP, double *ratio_PB, double *xP) {
    double m = Ay - yP;  /* vertical distance AP */
    double n = yP - By;  /* vertical distance PB */

    if (m + n == 0.0) {
        /* degenerate: cannot determine location */
        fprintf(stderr, "Error: m + n == 0, cannot compute section.\n");
        if (ratio_AP) *ratio_AP = 0.0;
        if (ratio_PB) *ratio_PB = 0.0;
        if (xP) *xP = 0.0;
        return;
    }

    if (ratio_AP) *ratio_AP = m;
    if (ratio_PB) *ratio_PB = n;

    /* Section formula for internal division:
       x = (n*Ax + m*Bx) / (m + n)
       (because AP:PB = m:n, weight on A is n, on B is m)
    */
    if (xP) *xP = (n*Ax + m*Bx) / (m + n);
}

