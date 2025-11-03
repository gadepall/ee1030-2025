#include <stdio.h>

void line_vectors(double slope, double* mvec, double* nvec) {
    mvec[0] = 1.0;
    mvec[1] = slope;
    nvec[0] = -slope;
    nvec[1] = 1.0;
}
