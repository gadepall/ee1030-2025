#include <math.h>
void function(double *p, double *n) {
    double magnitude = sqrt(pow(p[0], 2) + pow(p[1], 2) + pow(p[2], 2));
    n[0] = p[0] / magnitude;
    n[1] = p[1] / magnitude;
    n[2] = p[2] / magnitude;
}
