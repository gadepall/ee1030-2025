#include <stdio.h> 

void calculate_section_point(double* result_x, double* result_y) {
    // Variable values are taken directly from your C code.
    int x1 = -4, x2 = 0, y1 = 0, y2 = 6;
    double k1 = 3.0 / 4.0; // weight for point B (x2, y2)
    double k2 = 1.0 / 4.0; // weight for point A (x1, y1)

    *result_x = k1 * x2 + k2 * x1;
    *result_y = k1 * y2 + k2 * y1;
}