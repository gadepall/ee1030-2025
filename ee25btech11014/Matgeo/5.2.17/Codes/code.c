#include <stdio.h>

// Solve system of equations:
// x - 3y = 7
// 3x - 3y = 15
//
// Returns solution in sol[0] = x, sol[1] = y
void solve_system(double sol[2]) {
    double a11 = 1, a12 = -3, b1 = 7;
    double a21 = 3, a22 = -3, b2 = 15;

    double det = a11 * a22 - a12 * a21;

    sol[0] = (b1 * a22 - a12 * b2) / det;  // x
    sol[1] = (a11 * b2 - b1 * a21) / det;  // y
}
