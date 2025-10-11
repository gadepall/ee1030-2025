#include <stdio.h>
#include <math.h>

double root1(double a, double b, double c) {
    double d = b*b - 4*a*c;
    return (-b + sqrt(d)) / (2*a);
}

double root2(double a, double b, double c) {
    double d = b*b - 4*a*c;
    return (-b - sqrt(d)) / (2*a);
}
