#include <stdio.h>

void get_lines(double* x, double* y1, double* y2, int n) {
    for (int i = 0; i < n; i++) {
        y1[i] = x[i] - 8; 
        y2[i] = x[i] - 16.0/3.0; 
    }
}
