// ac.c
#include <stdio.h>

void compute_AC(double a[], double b[], double result[], int n) {
    for (int i = 0; i < n; i++) {
        result[i] = 3*b[i] - 2*a[i];
    }
}

