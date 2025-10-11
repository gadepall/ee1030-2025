#include <math.h>
void function(double r, double d, double *q1_x, double *q1_y, double *q2_x, double *q2_y) {
    if (d < r) {
        *q1_x = *q1_y = *q2_x = *q2_y = 0.0;
        return;
    }
    double x_coord = (r * r) / d;
    double y_coord_abs = (r / d) * sqrt((d * d) - (r * r));
    *q1_x = x_coord;
    *q1_y = y_coord_abs;
    *q2_x = x_coord;
    *q2_y = -y_coord_abs;
}
