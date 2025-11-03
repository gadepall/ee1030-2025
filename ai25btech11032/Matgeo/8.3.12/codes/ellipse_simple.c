#include <math.h>

void ellipse_params(const double *F1, const double *F2, double sum,
                    double *V, double *u, double *f,
                    double *c, double *a_out, double *b_out)
{
    // center
    c[0] = 0.5 * (F1[0] + F2[0]);
    c[1] = 0.5 * (F1[1] + F2[1]);

    // a, cf, b
    double a = 0.5 * sum;
    double dx = F2[0] - F1[0];
    double dy = F2[1] - F1[1];
    double cf = 0.5 * sqrt(dx*dx + dy*dy);
    double b2 = a*a - cf*cf;
    double b  = sqrt(b2);

    if (a_out) *a_out = a;
    if (b_out) *b_out = b;

    // V = diag(1/a^2, 1/b^2)
    V[0] = 1.0/(a*a); V[1] = 0.0;
    V[2] = 0.0;       V[3] = 1.0/(b*b);

    // u = -V c
    u[0] = -(V[0]*c[0] + V[1]*c[1]);
    u[1] = -(V[2]*c[0] + V[3]*c[1]);

    // f = c^T V c - 1
    *f = c[0]*(V[0]*c[0] + V[1]*c[1]) + c[1]*(V[2]*c[0] + V[3]*c[1]) - 1.0;
}

