#include <stdio.h>
#include <math.h>

int findYCoordinates(double px, double py, double qx, double d, double *y1, double *y2) {
    double term = pow(d, 2) - pow(qx - px, 2);
    double sqrt_term = sqrt(term);
    *y1 = py + sqrt_term;
    *y2 = py - sqrt_term;
    
    return 1; 
}

