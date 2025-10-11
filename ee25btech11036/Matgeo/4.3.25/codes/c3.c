// ratio.c
#include <stdio.h>
#include <math.h>

void yz_plane_ratio(double x1, double y1, double z1,
                     double x2, double y2, double z2,
                     double *t_out, double *one_minus_t_out)
{
    if (x2 == x1) {
        // line parallel to YZ-plane in x-direction -> x constant
        *t_out = NAN;
        *one_minus_t_out = NAN;
        return;
    }
    double t = -x1 / (x2 - x1);  // from (1-t)*x1 + t*x2 = 0 -> t = -x1/(x2-x1)
    *t_out = t;
    *one_minus_t_out = 1.0 - t;
}

/* Optional test main (not used when building .so)
int main(void) {
    double t, omt;
    yz_plane_ratio(-2,4,7, 3,-5,8, &t, &omt);
    printf("t = %g, 1-t = %g\n", t, omt);
    return 0;
}
*/
