// lines.c
#include <math.h>

// Return lambda for which the two lines are perpendicular.
double perpendicular_lambda(void) {
    return 1.0;
}

// Return lambda for which the two lines intersect.
double intersection_lambda(void) {
    return -35.0/19.0;
}

// For a given lambda, check whether the two lines intersect.
// Writes s (parameter of line2) and t (parameter of line1) to the output pointers.
// Returns 1 if intersection exists (within tolerance), otherwise 0.
int lines_intersection_params(double lambda, double *s_out, double *t_out) {
    const double EPS = 1e-9;
    double denom1 = 1.0 - 3.0*(5.0*lambda + 2.0);
    if (fabs(denom1) < EPS) return 0;
    double s1 = 5.0/denom1;
    double denom2 = 30.0 + 4.0*lambda;
    if (fabs(denom2) < EPS) return 0;
    double s2 = 5.0/denom2;
    if (fabs(s1 - s2) > 1e-6) return 0;
    double s = 0.5*(s1 + s2);
    double t = 3.0*s;
    if (s_out) *s_out = s;
    if (t_out) *t_out = t;
    return 1;
}
