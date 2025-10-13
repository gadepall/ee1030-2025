/* planes.c
   Build: gcc -shared -fPIC -o libplanes.so planes.c -lm
*/

#include <math.h>

void equal_inclined_planes(double distance, double *coeffs_out)
{
    if (!coeffs_out) return;
    if (distance < 0) distance = -distance;

    double a = 1.0, b = 1.0, c = 1.0;
    double rhs = distance * sqrt(3.0);

    coeffs_out[0] = a; coeffs_out[1] = b; coeffs_out[2] = c; coeffs_out[3] =  rhs;
    coeffs_out[4] = a; coeffs_out[5] = b; coeffs_out[6] = c; coeffs_out[7] = -rhs;
}
