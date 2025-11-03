#include <stdio.h>

void solve_system(double aug[2][3], double *x, double *y) {
    double a1 = aug[0][0], b1 = aug[0][1], c1 = aug[0][2];
    double a2 = aug[1][0], b2 = aug[1][1], c2 = aug[1][2];

    double det  = a1*b2 - a2*b1;
    double detx = c1*b2 - c2*b1;
    double dety = a1*c2 - a2*c1;

    if(det == 0) {
        *x = *y = 0; // No unique solution
        return;
    }

    *x = detx / det;
    *y = dety / det;
}

