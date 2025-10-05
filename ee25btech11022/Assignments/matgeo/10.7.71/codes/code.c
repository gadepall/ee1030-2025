// code.c
#include <stdio.h>
#include <math.h>

// Output: pts[9] = [O_x, O_y, A_x, A_y, P_x, P_y, T_x, T_y, N_x, N_y]
// O: origin, A: tangent-X, P: point, T: tangent(another), N: normal(another)
void get_points(double* pts) {
    // O = (0, 0)
    pts[0] = 0.0; pts[1] = 0.0;

    // A = tangent with X axis: (4,0)
    pts[2] = 4.0; pts[3] = 0.0;

    // P = (1, sqrt(3))
    pts[4] = 1.0; pts[5] = sqrt(3.0);

    // Compute direction vectors:
    // Tangent at P is x + sqrt(3)y = 4
    // Let y = t, x = 4 - sqrt(3)t; giving (x, y) = (4-sqrt(3)t, t)
    // Choose t1 = 0 for intersection A, and t2 = 2 for below intersection B
    // B = (4 - sqrt(3)*2, 2) = (4 - 2*1.73205, 2) ~ (0.5359, 2)
    pts[6] = 4.0 - sqrt(3.0)*2.0;
    pts[7] = 2.0;

    // Normal: line through O and P, param t, (t, t*sqrt(3))
    // With x axis, y=0 => t=0 (origin)
    // With y axis, x=0 => y=0 (again origin), for plotting purpose get a point far from origin t=2
    pts[8] = 2.0;
    pts[9] = 2.0*sqrt(3.0);
}


