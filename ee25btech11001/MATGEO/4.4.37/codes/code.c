// code.c
#include <stdio.h>
#include <math.h>

// Function to compute m vector (equal angle with axes)
void get_m(double *mx, double *my, double *mz) {
    double val = 1.0 / sqrt(3.0);
    *mx = val;
    *my = val;
    *mz = val;
}

