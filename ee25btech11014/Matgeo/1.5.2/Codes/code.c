#include <stdio.h>

// Section formula: returns y-coordinate when x=0
float sec_form(int x1, int y1, int x2, int y2, int *m, int *n, float *px, float *py) {
    // Compute ratio
    *m = x1;
    *n = -x2;

    // Point of intersection (x=0)
    *px = 0.0;
    *py = (*m * y2 + *n * y1) / (float)(*m + *n);

    return *py;
}
