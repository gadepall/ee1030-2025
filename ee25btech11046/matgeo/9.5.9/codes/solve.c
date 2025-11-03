#include <math.h>
void function(double a, double b, double c, double *root1, double *root2) {
    *root1 = (-b - sqrt(b*b - 4*a*c))/(2*a);
    *root2 = (-b + sqrt(b*b - 4*a*c))/(2*a);
}
