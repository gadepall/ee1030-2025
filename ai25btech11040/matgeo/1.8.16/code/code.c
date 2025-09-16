#include <math.h>
double vec_x(double x, double y, double m) {
    return x/sqrt(x*x+y*y)*m;
}
double vec_y(double x, double y, double m) {
    return y/sqrt(x*x+y*y)*m;
}