#include <stdlib.h>

// Fill arrays with coordinates of Line 1: (1+2t, -1+3t, 1+4t)
// and Line 2: (3+t, k+2t, t)
// Inputs: t_min, t_max, n_points, k
// Outputs: arrays (x1,y1,z1,x2,y2,z2)
void generate_lines(double t_min, double t_max, int n_points, double k,
                    double *x1, double *y1, double *z1,
                    double *x2, double *y2, double *z2) {
    double step = (t_max - t_min) / (n_points - 1);

    for (int i = 0; i < n_points; i++) {
        double t = t_min + i * step;

        // Line 1
        x1[i] = 1 + 2*t;
        y1[i] = -1 + 3*t;
        z1[i] = 1 + 4*t;

        // Line 2
        x2[i] = 3 + t;
        y2[i] = k + 2*t;
        z2[i] = t;
    }
}
