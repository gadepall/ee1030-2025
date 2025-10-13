#include <math.h>
#include <stdio.h>

void compute_tangents(double h, double k, double r,
                      double x1, double y1,
                      double *out)
{
    double vx = x1 - h;
    double vy = y1 - k;
    double d = hypot(vx, vy);

    if (d <= r + 1e-12) {
        out[0] = 0.0;
        for (int i=1;i<9;i++) out[i] = NAN;
        return;
    }

    double ux0 = vx / d;
    double uy0 = vy / d;

    double cos_phi = r / d;
    if (cos_phi > 1.0) cos_phi = 1.0;
    if (cos_phi < -1.0) cos_phi = -1.0;
    double phi = acos(cos_phi);

    double cos_p = cos(phi), sin_p = sin(phi);

    double u1x = ux0 * cos_p - uy0 * sin_p;
    double u1y = ux0 * sin_p + uy0 * cos_p;

    double u2x = ux0 * cos_p + uy0 * sin_p;
    double u2y = -ux0 * sin_p + uy0 * cos_p;

    double xt1 = h + r * u1x;
    double yt1 = k + r * u1y;
    double xt2 = h + r * u2x;
    double yt2 = k + r * u2y;

    double m1, c1, m2, c2;
    const double EPS = 1e-12;
    if (fabs(xt1 - x1) < EPS) { m1 = HUGE_VAL; c1 = xt1; } else {
        m1 = (yt1 - y1) / (xt1 - x1);
        c1 = y1 - m1 * x1;
    }
    if (fabs(xt2 - x1) < EPS) { m2 = HUGE_VAL; c2 = xt2; } else {
        m2 = (yt2 - y1) / (xt2 - x1);
        c2 = y1 - m2 * x1;
    }

    double x[4] = { h, xt1, x1, xt2 };
    double y[4] = { k, yt1, y1, yt2 };
    double S = 0.0;
    for (int i=0;i<4;i++){
        int j = (i+1)%4;
        S += x[i]*y[j] - x[j]*y[i];
    }
    double area = fabs(S) * 0.5;

    out[0] = area;
    out[1] = xt1; out[2] = yt1;
    out[3] = m1;  out[4] = c1;
    out[5] = xt2; out[6] = yt2;
    out[7] = m2;  out[8] = c2;
}
