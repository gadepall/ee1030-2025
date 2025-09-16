#include <stdio.h>
void add_three_arrays(double *a, double *b, double *c, double *result) {
    for (int i = 0; i < 3; i++) {
        result[i] = a[i] + b[i] + c[i];
    }
}

