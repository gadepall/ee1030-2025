#include <stdio.h>

// Function to solve the 2x2 system:
// x - y = 26
// x - 3y = 0
void solve_system(double* x, double* y) {
    double a1 = 1, b1 = -1, c1 = 26;
    double a2 = 1, b2 = -3, c2 = 0;

    double det = a1*b2 - a2*b1;
    if(det != 0) {
        *x = (c1*b2 - c2*b1)/det;
        *y = (a1*c2 - a2*c1)/det;
    } else {
        *x = 0;
        *y = 0;
    }
}
