#include <stdio.h>

void check_parabola(double *x, double *y, int n, double t_min, double t_max) {
    double step = (t_max - t_min) / (n - 1);
    double t;

    for (int i = 0; i < n; i++) {
        t = t_min + i * step;
        x[i] = t * t + t + 1;
        y[i] = t * t - t + 1;
    }

    
    double A = 1, B = -2, C = 1;
    double discriminant = B*B - 4*A*C;

    if (discriminant == 0)
        printf("Parabola\n");
    else
        printf("Not a Parabola\n");
}

