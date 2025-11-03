#include<math.h>

int find_y(double x1, double y1, double x2, double d, double *y_out1, double *y_out2) {
    double dx = x1 - x2;
    double inside = d * d - dx * dx; /* (y1 - y)^2 = inside */

    if (inside < 0.0) {
        /* No real solutions */
        return 0;
    } else if (inside == 0.0) {
        /* exactly one solution (double root) */
        *y_out1 = y1;
        *y_out2 = y1;
        return 1;
    } else {
        double r = sqrt(inside);
        *y_out1 = y1 + r;
        *y_out2 = y1 - r;
        return 2;
    }
}
