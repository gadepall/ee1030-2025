#include <stdio.h>
#include <math.h>
void line_equation(double m, double px, double py, double *a, double *b, double *c) {
    if (isinf(m)) {
        *a = 1;
        *b = 0;
        *c = -px;
    } else {
        *a = -m;
        *b = 1;
        *c = -( (*a)*px + (*b)*py );
    }
}