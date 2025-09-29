 #include <math.h>

void unit_vector3d(double *x, double *y, double *z) {
    double mag = sqrt((*x)*(*x) + (*y)*(*y) + (*z)*(*z));
    if (mag == 0) return; // avoid division by zero
    *x /= mag;
    *y /= mag;
    *z /= mag; 
    }
