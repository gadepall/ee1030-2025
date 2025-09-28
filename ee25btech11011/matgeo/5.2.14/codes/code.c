#include <stdio.h>

int solve(int a1, int b1, int c1, int a2, int b2, int c2, float* x, float* y) {
    int det = a1 * b2 - a2 * b1;

    if (det == 0) {
        if (a1 * c2 == a2 * c1 && b1 * c2 == b2 * c1)
            return 2; // coincident
        else
            return 1; // parallel
    } else {
        *x = (float)(c1 * b2 - c2 * b1) / det;
        *y = (float)(a1 * c2 - a2 * c1) / det;
        return 0; // unique solution
    }
}
