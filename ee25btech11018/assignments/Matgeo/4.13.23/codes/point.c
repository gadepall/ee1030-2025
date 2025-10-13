#include <stdio.h>

// Function to compute x from first line
double computeX1(double a, double c) {
    return -c / (2.0 * a);
}

// Function to compute x from second line
double computeX2(double b, double d) {
    return -d / (3.0 * b);
}

// Function to compute y (since y = -x for equidistant from axes in 4th quadrant)
double computeY(double x) {
    return -x;
}

// Function to check relation 3bc - 2ad = 0
int checkRelation(double a, double b, double c, double d) {
    double relation = 3*b*c - 2*a*d;
    return (relation == 0) ? 1 : 0;
}

