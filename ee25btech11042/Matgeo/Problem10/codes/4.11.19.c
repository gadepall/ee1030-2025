
#include <stdio.h>
void calculate_plot_data(const double* p, const double* q,
                         double* intersection_point,
                         double* line_segment_x,
                         double* line_segment_y,
                         double* line_segment_z,
                         int num_line_points) {
    // Direction vector d = q - p
    double d[3];
    d[0] = q[0] - p[0]; // dx
    d[1] = q[1] - p[1]; // dy
    d[2] = q[2] - p[2]; // dz

    // Find lambda for intersection with the XZ plane (where y=0)
    // y(lambda) = p[1] + lambda * d[1] = 0  =>  lambda = -p[1] / d[1]
    double lambda_intersect = -p[1] / d[1];

    // Calculate and store the intersection point
    intersection_point[0] = p[0] + lambda_intersect * d[0];
    intersection_point[1] = 0.0; // By definition of the XZ plane
    intersection_point[2] = p[2] + lambda_intersect * d[2];

    // Define a range for the parameter lambda to plot a nice segment of the line
    double lambda_start = -1.0;
    double lambda_end = 2.5;
    double lambda_step = (lambda_end - lambda_start) / (num_line_points - 1);

    // Generate points for the line segment
    for (int i = 0; i < num_line_points; ++i) {
        double lambda = lambda_start + i * lambda_step;
        line_segment_x[i] = p[0] + lambda * d[0];
        line_segment_y[i] = p[1] + lambda * d[1];
        line_segment_z[i] = p[2] + lambda * d[2];
    }
}


