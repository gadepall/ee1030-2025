#include <stdio.h>
#include <math.h>

double solve_angle(double qx, double qy, double rx, double ry) {
    double q_norm = sqrt(qx*qx + qy*qy);
    double r_norm = sqrt(rx*rx + ry*ry);

    double dot = qx*rx + qy*ry;

    double cos_theta = dot / (q_norm * r_norm);
    double theta = acos(cos_theta);

    double angle = theta / 2.0;
    return angle;
}


