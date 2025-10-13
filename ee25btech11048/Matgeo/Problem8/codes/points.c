#include <stdio.h>
#include <math.h>

// Function to compute distance between A(1,-2,9) and P(7,6,9)
double compute_distance() {
    double A[3] = {1, -2, 9};
    double P[3] = {7, 6, 9};
    double v[3];
    double sum = 0.0;

    for(int i=0; i<3; i++) {
        v[i] = P[i] - A[i];
        sum += v[i]*v[i];
    }

    return sqrt(sum);
}

