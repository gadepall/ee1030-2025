#include <stdio.h>

void find_intercepts(double *x_int, double *y_int, double *z_int,double a,double b,double c,double d) {
    // Plane equation: ax + by + cz = d
    // X-intercept -> y=0, z=0 -> ax=d 
    *x_int = d / a;

    // Y-intercept -> x=0, z=0 -> by-d=0 
    *y_int = d / b;

    // Z-intercept -> x=0, y=0 -> cz-d=0 
    *z_int = d / c;
}