// solve_medians.c
#include "median_utils.h"

void solve_medians(double* coords, double* medians) {
    double Ax = coords[0], Ay = coords[1];
    double Bx = coords[2], By = coords[3];
    double Cx = coords[4], Cy = coords[5];

    double mx, my;

    // A → midpoint of BC
    compute_midpoint(Bx, By, Cx, Cy, &mx, &my);
    medians[0] = Ax; medians[1] = Ay;
    medians[2] = mx; medians[3] = my;

    // B → midpoint of AC
    compute_midpoint(Cx, Cy, Ax, Ay, &mx, &my);
    medians[4] = Bx; medians[5] = By;
    medians[6] = mx; medians[7] = my;

    // C → midpoint of AB
    compute_midpoint(Ax, Ay, Bx, By, &mx, &my);
    medians[8] = Cx; medians[9] = Cy;
    medians[10] = mx; medians[11] = my;
}
