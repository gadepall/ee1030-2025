
#include <stdio.h>

void get_circle_params(double* out_data) {
    // Given circle: x^2 + y^2 - 6x - 6y + 14 = 0
    // Centre: (3,3), radius = 2
    out_data[0] = 3.0;   // x-coordinate
    out_data[1] = 3.0;   // y-coordinate
    out_data[2] = 2.0;   // radius
}

