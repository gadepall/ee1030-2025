#include <stdio.h>
void calculate_slopes(double intercept_a, double* output_slopes) {
    // A line requires non-zero intercepts. If a is zero, we can't calculate a slope.
    if (intercept_a == 0.0) {
        output_slopes[0] = 0.0; // Or some error value like NAN
        output_slopes[1] = 0.0;
        return;
    }
 double slope1 = intercept_a / (-intercept_a);
 double slope2 = (-intercept_a) / (-intercept_a);
    // Fill the output array with the two calculated slopes
    output_slopes[0] = slope1;
    output_slopes[1] = slope2;
}
