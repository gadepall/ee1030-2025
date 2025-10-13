#include <math.h>

double positiveeigenvalue(double a, double b, double c, double d) {
    double trace = a + d;
    double det = a*d - b*c;
    double discriminant = trace*trace - 4*det;
    double lambda1 = (trace + sqrt(discriminant)) / 2.0;
    double lambda2 = (trace - sqrt(discriminant)) / 2.0;

    if (lambda1 > 0) {
        return lambda1;
    }
    return lambda2;
}

