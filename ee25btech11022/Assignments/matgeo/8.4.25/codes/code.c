#include <stdio.h>

void get_parabola_data(double *vertex, double *p, double *directrix_x) {
    // vertex (1/2, -2)
    vertex[0] = 0.5;
    vertex[1] = -2.0;

    // parameter p = 3/4
    *p = 0.75;

    // directrix x = vertex_x + p
    *directrix_x = vertex[0] + *p;
}

