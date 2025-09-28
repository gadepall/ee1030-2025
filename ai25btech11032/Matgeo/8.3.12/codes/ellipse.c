#include <math.h>

// Compute V (2x2, row-major), u (2), f from foci F1,F2 and sum (=2a).
//   c = (F1+F2)/2
//   a = sum/2
//   c_f = ||F2-F1||/2,  b^2 = a^2 - c_f^2
//   D = diag(1/a^2, 1/b^2)   [axis-aligned for this problem]
//   V = D
//   u = -V c
//   f = c^T V c - 1
void ellipse_vuf(const double *F1, const double *F2, double sum,
                 double *V, double *u, double *f)
{
    // center
    double cx = (F1[0] + F2[0]) / 2.0;
    double cy = (F1[1] + F2[1]) / 2.0;

    // a, c_f, b
    double a  = sum / 2.0;
    double dx = F2[0] - F1[0];
    double dy = F2[1] - F1[1];
    double cf = sqrt(dx*dx + dy*dy) / 2.0;
    double b2 = a*a - cf*cf;
    double b  = sqrt(b2);

    // D = diag(1/a^2, 1/b^2)
    double D00 = 1.0/(a*a);
    double D11 = 1.0/(b*b);

    // V = D (axis-aligned for this question)
    V[0] = D00; V[1] = 0.0;
    V[2] = 0.0; V[3] = D11;

    // u = -V c
    u[0] = -(V[0]*cx + V[1]*cy);
    u[1] = -(V[2]*cx + V[3]*cy);

    // f = c^T V c - 1
    *f = cx*(V[0]*cx + V[1]*cy) + cy*(V[2]*cx + V[3]*cy) - 1.0;
}

