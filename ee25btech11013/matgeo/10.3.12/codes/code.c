#include <math.h>

double compute_x() {
    return 8 * sqrt(3);
}

double compute_y(double x) {
    return (x * x) / 16.0;
}

double compute_k(double x, double y) {
    return y - sqrt(3) * x;
}

