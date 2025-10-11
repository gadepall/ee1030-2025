#include <stdio.h>
#include <stdlib.h>

void generate_plane1(double *Y, double *Z, double *X, int N) {
    for(int i = 0; i < N*N; i++) {
        X[i] = 2 * Y[i];
    }
}

void generate_plane2(double *X, double *Z, double *Y, int N) {
    for(int i = 0; i < N*N; i++) {
        Y[i] = 0;
    }
}

void generate_intersection_line(double *x, double *y, double *z, int N) {
    double dz = 4.0/(N-1);
    for(int i = 0; i < N; i++) {
        x[i] = 0;
        y[i] = 0;
        z[i] = -2 + i*dz;
    }
}
