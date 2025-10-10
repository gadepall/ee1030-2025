#include <stdio.h>


void rotate_vector(double original_vec[3], double rotated_vec[3]) {
    rotated_vec[0] = original_vec[0];
    rotated_vec[1] = original_vec[2];
    rotated_vec[2] = -original_vec[1];
}


void generate_points(double vector[3], int num_points, double* points_out) {
    if (num_points <= 1) {
        if (num_points == 1) {
            points_out[0] = vector[0];
            points_out[1] = vector[1];
            points_out[2] = vector[2];
        }
        return;
    }

    for (int i = 0; i < num_points; ++i) {
        // Create a linear interpolation factor 't' from 0.0 to 1.0
        double t = (double)i / (double)(num_points - 1);

        // Calculate the coordinates for the point at 't'
        points_out[i * 3 + 0] = vector[0] * t; // x
        points_out[i * 3 + 1] = vector[1] * t; // y
        points_out[i * 3 + 2] = vector[2] * t; // z
    }
}
