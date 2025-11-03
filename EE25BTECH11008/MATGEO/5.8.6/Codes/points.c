#include <stdio.h>

void get_lines(double* x, double* y1, double* y2, int n) {
    for (int i = 0; i < n; i++) {
        y1[i] = 3*x[i] - 3.0; 
        y2[i] = 4*x[i] - 8.0; 
    }
}
