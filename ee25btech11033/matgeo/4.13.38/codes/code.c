
#include <stdio.h>

void calculate_plot_values(double px, double py,
                           double qx, double qy,
                           double rx, double ry,
                           double ppx, double ppy,
                           double* out_sx, double* out_sy,
                           double* out_a, double* out_b, double* out_c) {
    *out_sx = (qx + rx) / 2.0;
    *out_sy = (qy + ry) / 2.0;
    double vec_ps_x = *out_sx - px;
    double vec_ps_y = *out_sy - py;
    *out_a = -vec_ps_y;
    *out_b = vec_ps_x;
    *out_c = -((*out_a) * ppx + (*out_b) * ppy);
}

