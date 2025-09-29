#include <stdio.h>

typedef struct {
    double x, y, z;
} Point;

// Generate points array for A, B, C
void generate_plane_points(double a, double b, double c, double *points_array) {
    points_array[0] = a; points_array[1] = 0; points_array[2] = 0; // A
    points_array[3] = 0; points_array[4] = b; points_array[5] = 0; // B
    points_array[6] = 0; points_array[7] = 0; points_array[8] = c; // C
}

// Compute k
double compute_plane_k(double a, double b, double c) {
    double x = a/3.0, y = b/3.0, z = c/3.0;
    return 1.0/(x*x) + 1.0/(y*y) + 1.0/(z*z);
}

