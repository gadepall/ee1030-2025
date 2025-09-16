
#include <math.h>


void find_points(double* p1_x, double* p1_y, double* p2_x, double* p2_y) {
    // The problem simplifies to solving |k + 2| = 5 for a parameterized
    // point (k, 4-k) on the line x+y=4.
    
    // Case 1: k + 2 = 5  => k = 3
    double k1 = 3.0;
    *p1_x = k1;
    *p1_y = 4.0 - k1; // y = 4 - 3 = 1

    // Case 2: k + 2 = -5 => k = -7
    double k2 = -7.0;
    *p2_x = k2;
    *p2_y = 4.0 - k2; // y = 4 - (-7) = 11
}
