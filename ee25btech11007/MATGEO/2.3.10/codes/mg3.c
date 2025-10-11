#include <math.h>

int solve_angle_simple(const double *a, const double *b, int n, double *theta_deg) {
    const double SQRT2 = 1.4142135623730950488;
    const double PI    = 3.14159265358979323846;
    const double TOL   = 1e-9;

    double aa = 0.0, bb = 0.0, lhs_sq = 0.0;
    for (int i = 0; i < n; ++i) {
        aa += a[i] * a[i];
        bb += b[i] * b[i];
        double t = a[i] - SQRT2 * b[i];
        lhs_sq += t * t;
    }
    double na = sqrt(aa);
    double nb = sqrt(bb);
    double lhs = sqrt(lhs_sq);

    double ab = 0.0;
    for (int i = 0; i < n; ++i) ab += a[i] * b[i];

    double denom = na * nb;
    double cos_theta = (denom > 0.0) ? (ab / denom) : 1.0;
    if (cos_theta >  1.0) cos_theta =  1.0;
    if (cos_theta < -1.0) cos_theta = -1.0;
    *theta_deg = acos(cos_theta) * (180.0 / PI);

    if (fabs(na - 1.0) <= TOL && fabs(nb - 1.0) <= TOL && fabs(lhs - 1.0) <= TOL) {
        *theta_deg = 45.0;
        return 0;
    }
    return 1;
}
