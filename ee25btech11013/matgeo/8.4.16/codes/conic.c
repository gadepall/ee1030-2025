#include <math.h>


double ellipse_eccentricity(double a, double b) {
    return sqrt(1.0 - (b*b) / (a*a));
}

double hyperbola_eccentricity(double a, double b) {
    return sqrt(1.0 + (b*b) / (a*a));
}

double ellipse_focus(double a, double b) {
    return sqrt(a*a - b*b);
}

double hyperbola_focus(double a, double b) {
    return sqrt(a*a + b*b);
}

