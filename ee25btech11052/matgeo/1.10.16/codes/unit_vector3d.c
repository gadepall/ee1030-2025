#include <math.h>

void unit_vector3d(double *x, double *y, double *z) {
    double norm = sqrt((*x) * (*x) + (*y) * (*y) + (*z) * (*z));
    if (norm > 1e-9) {
        *x = *x / norm;
        *y = *y / norm;
        *z = *z / norm;
    }
}
