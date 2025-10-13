#include <stdio.h>

void GSM(double x[3], double a[3], double b[3], double c[3], double d[3]) {
        x[0] = (d[0] - b[0] * x[1] - c[0] * x[2]) / a[0];
        x[1] = (d[1] - a[1] * x[0] - c[1] * x[2]) / b[1];
        x[2] = (d[2] - b[2] * x[1] - a[2] * x[0]) / c[2];
    
}

