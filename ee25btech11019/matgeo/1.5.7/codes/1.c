#include <stdio.h>

double find_a(int x1, int y1, int x2, int y2, int given_y)
{
    double mid_x = (x1 + x2) / 2.0;
    // given midpoint is (a/4, given_y)
    return 4 * mid_x;
}