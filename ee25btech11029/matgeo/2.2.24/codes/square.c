#include <stdio.h>

// Fill the array with square vertices: A(1,7), B(4,2), C(-1,-1), D(-4,4)
void get_square_points(double *points) {
    double coords[8] = {1,7,  4,2,  -1,-1,  -4,4};

    for (int i = 0; i < 8; i++) {
        points[i] = coords[i];
    }
}
