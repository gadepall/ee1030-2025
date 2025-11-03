#include<math.h>

double angle_between(double p, double q, double r, double s) {
    double numerator   = - (p*p + q*q - r*r - s*s);
    double denominator = 2.0 * (p*q - r*s);
    double cos_theta   = numerator / denominator;
    return acos(cos_theta);
}