#include <stdio.h>

// Function to calculate 'a' (x-intercept) and 'b' (y-intercept)
// given the midpoint (xm, ym) of the line segment intercepted between the axes.
void findIntercepts(double xm, double ym, double *a, double *b) {
    // If the midpoint of (a, 0) and (0, b) is (xm, ym):
    // (a + 0) / 2 = xm  -> a = 2 * xm
    // (0 + b) / 2 = ym  -> b = 2 * ym
    *a = 2 * xm;
    *b = 2 * ym;
}