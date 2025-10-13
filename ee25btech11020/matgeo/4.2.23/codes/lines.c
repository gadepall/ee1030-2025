#include <stdio.h>

// Function takes arrays coeffs1[3] and coeffs2[3]
int are_perpendicular(double coeffs1[3], double coeffs2[3]) {
    double a1 = coeffs1[0], b1 = coeffs1[1];
    double a2 = coeffs2[0], b2 = coeffs2[1];

    double dot = a1*a2 + b1*b2;
    if(dot == 0.0) {
        return 1; // perpendicular
    }
    return 0; // not perpendicular
}

