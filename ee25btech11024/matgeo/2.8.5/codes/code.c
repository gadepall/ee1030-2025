#include <stdio.h>

void find_cube(double n, double *dir_vec, double len_par, double *cube_pts, double *start, double *end) {
    // Define the 8 cube points
    double pts[8][3] = {
        {0, 0, 0}, {n, 0, 0}, {n, 0, n}, {0, 0, n}, // bottom face
        {0, n, 0}, {n, n, 0}, {n, n, n}, {0, n, n}  // top face
    };

    // Copy points to output array (flattened)
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 3; j++) {
            cube_pts[i*3 + j] = pts[i][j];
        }
    }

    // Compute center of the cube
    double center[3] = { n/2, n/2, n/2 };

    // Compute start and end points of the line
    for (int i = 0; i < 3; i++) {
        start[i] = center[i] - len_par * dir_vec[i];
        end[i]   = center[i] + len_par * dir_vec[i];
    }
}
