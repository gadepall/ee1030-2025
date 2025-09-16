#include <stdio.h>

// Function: solve_tangents
// Input: r, h
// Output: tangents[4] = {a1, b1, a2, b2}
// Lines are: a1*x + b1*y = 0  and  a2*x + b2*y = 0
void solve_tangents(double r, double h, double tangents[4]) {
    // First tangent: x = 0 -> line (1,0)
    tangents[0] = 1.0;
    tangents[1] = 0.0;

    // Second tangent: (h^2 - r^2)x - 2rh y = 0
    double a = h*h - r*r;
    double b = -2.0*r*h;

    if (a == 0 && b == 0) {
        // Special case -> y=0
        tangents[2] = 0.0;
        tangents[3] = 1.0;
    } else {
        tangents[2] = a;
        tangents[3] = b;
    }
}

