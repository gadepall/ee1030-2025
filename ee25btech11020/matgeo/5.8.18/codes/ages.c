#include <stdio.h>

int solve2x2(double a11, double a12, double a21, double a22,
             double b1, double b2, double sol[2]) {
    double det = a11*a22 - a12*a21;
    if(det == 0.0) {
        return -1; // No unique solution
    }

    sol[0] = (b1*a22 - b2*a12) / det; // x1
    sol[1] = (a11*b2 - a21*b1) / det; // x2
    return 0;
}

