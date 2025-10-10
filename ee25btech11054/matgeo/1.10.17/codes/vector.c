#include <stdio.h>

void generate_points(double vector[3], int n, double *points) {
    for (int i = 0; i < n; i++) {
        double t = (double)i / (n - 1);  // from 0 to 1
        points[3*i + 0] = t * vector[0];
        points[3*i + 1] = t * vector[1];
        points[3*i + 2] = t * vector[2];
    }
}

