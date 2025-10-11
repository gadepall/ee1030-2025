#include <math.h>


double arr_dot(const double *u, const double *v, int n) {
    double sum = 0.0;
    for (int i = 0; i < n; ++i) sum += u[i] * v[i];
    return sum;
}

double arr_norm(const double *u, int n) {
    double s = arr_dot(u, u, n);
    if (s <= 0.0) return 0.0;
    return sqrt(s);
}

void arr_scale(const double *u, double k, double *out, int n) {
    for (int i = 0; i < n; ++i) out[i] = k * u[i];
}

void arr_normalize(const double *u, double *out, int n) {
    double r = arr_norm(u, n);
    if (r == 0.0) {
        for (int i = 0; i < n; ++i) out[i] = 0.0;
    } else {
        for (int i = 0; i < n; ++i) out[i] = u[i] / r;
    }
}

/* -------- Line solver: ax + by = c --------
   normal  = (a, b)
   direction = (-b, a)  (perpendicular to normal)
*/
void line_direction_normal(double a, double b, double c,
                           double *dir_out,      /* length 2 */
                           double *normal_out) { /* length 2 */
    (void)c;               /* c isn't needed for vectors */
    normal_out[0] = a;     normal_out[1] = b;
    dir_out[0]    = -b;    dir_out[1]    = a;
}
