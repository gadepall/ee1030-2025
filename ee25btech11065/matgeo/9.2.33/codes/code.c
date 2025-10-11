#include <stdio.h>

double calculate_area() {
    double upper_bound_integral = (2.0 * 2.0 / 2.0) + (2.0 * 2.0) - (2.0 * 2.0 * 2.0 / 3.0);
    double lower_bound_integral = (-1.0 * -1.0 / 2.0) + (2.0 * -1.0) - (-1.0 * -1.0 * -1.0 / 3.0);
    return upper_bound_integral - lower_bound_integral;
}


