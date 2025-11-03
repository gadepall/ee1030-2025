#include <math.h>
double root(double x) {
    if (x < 0) return 0;
    return sqrt(x);
}
void function(const double V[], const double u[], double f, double h[], const double m[], double *kappa_out) {
    double v11 = V[0], v12 = V[1], v21 = V[2], v22 = V[3];
    double g_h = (h[0]*h[0]*v11 + (v12+v21)*h[0]*h[1] + h[1]*h[1]*v22) + 2*(u[0]*h[0] + u[1]*h[1]) + f;
    double m_V_m = m[0]*m[0]*v11 + (v12+v21)*m[0]*m[1] + m[1]*m[1]*v22;
    double Vh_plus_u[2];
    Vh_plus_u[0] = v11*h[0] + v12*h[1] + u[0];
    Vh_plus_u[1] = v21*h[0] + v22*h[1] + u[1];
    double m_Vh_u = m[0]*Vh_plus_u[0] + m[1]*Vh_plus_u[1];
    double A = m_V_m;
    double B = 2 * m_Vh_u;
    double C = g_h;
    double discriminant = B*B - 4*A*C;
    double k1 = (-B + root(discriminant)) / (2 * A);
    double k2 = (-B - root(discriminant)) / (2 * A);
    *kappa_out = (k1 > 0) ? k1 : k2;
}
