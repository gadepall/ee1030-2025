#include <stdio.h>
#include <math.h>

double getLatusRectumLowerBound() {
    // The boundary angle where eccentricity e = 2 is theta = pi/3.
    double theta = M_PI / 3.0;

    // latus rectum: l = 2 * sin^2(theta) / cos(theta)
    double sin_val = sin(theta);
    double cos_val = cos(theta);
    
    double lower_bound = (2 * pow(sin_val, 2)) / cos_val;

    return lower_bound;
}