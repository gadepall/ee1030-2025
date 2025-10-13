// simple_conic.c
// Build on Linux/macOS:  gcc -O2 -fPIC -shared -o libsimple_conic.so simple_conic.c
#include <math.h>

void intersect_line_conic(
    const double V[4],     // 2x2 row-major: [V00,V01,V10,V11]
    const double u[2],     // size-2
    double f,              // scalar
    const double h[2],     // line anchor
    const double m[2],     // line direction
    double kappa_out[2],   // outputs
    double x1[2],
    double x2[2],
    int *status            // 2=two real, 1=one (tangent), 0=none
) {
    double Vm0 = V[0]*m[0] + V[1]*m[1];
    double Vm1 = V[2]*m[0] + V[3]*m[1];
    double mTVm = m[0]*Vm0 + m[1]*Vm1;

    double Vh0 = V[0]*h[0] + V[1]*h[1];
    double Vh1 = V[2]*h[0] + V[3]*h[1];

    double Vh_u0 = Vh0 + u[0];
    double Vh_u1 = Vh1 + u[1];

    double mT_Vh_u = m[0]*Vh_u0 + m[1]*Vh_u1;

    double hTVh = h[0]*Vh0 + h[1]*Vh1;
    double two_uTh = 2.0*(u[0]*h[0] + u[1]*h[1]);
    double g = hTVh + two_uTh + f;

    double disc = mT_Vh_u*mT_Vh_u - g*mTVm;

    if (disc > 1e-12) {
        double r = sqrt(disc);
        kappa_out[0] = (-mT_Vh_u + r) / mTVm;
        kappa_out[1] = (-mT_Vh_u - r) / mTVm;
        x1[0] = h[0] + kappa_out[0]*m[0];  x1[1] = h[1] + kappa_out[0]*m[1];
        x2[0] = h[0] + kappa_out[1]*m[0];  x2[1] = h[1] + kappa_out[1]*m[1];
        *status = 2;
    } else if (fabs(disc) <= 1e-12) {
        kappa_out[0] = kappa_out[1] = (-mT_Vh_u) / mTVm;
        x1[0] = x2[0] = h[0] + kappa_out[0]*m[0];
        x1[1] = x2[1] = h[1] + kappa_out[0]*m[1];
        *status = 1;
    } else {
        *status = 0;
    }
}

