#ifndef LOCUS_H
#define LOCUS_H

#include <stdio.h>
#include <math.h>

// Function to compute standard form parameters
void standard_form(double A[3], double B[3], double constant_sum,
                   double *a2, double *b2, double *c2) {
    double dist_AB = sqrt(pow(A[0]-B[0],2) + pow(A[1]-B[1],2) + pow(A[2]-B[2],2));
    double a = constant_sum / 2.0;
    double c = dist_AB / 2.0;
    double b = sqrt(a*a - c*c);

    *a2 = a*a;
    *b2 = b*b;
    *c2 = b*b; // spheroid symmetry
}

#endif

