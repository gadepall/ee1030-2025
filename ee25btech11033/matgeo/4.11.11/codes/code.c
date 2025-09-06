// File: calculator.c
#include <math.h>
#include <stdio.h>

// This function takes coordinates for A and B, calculates the intersection P
// with the line x - 3y = 0, finds the ratio, and prepares data for plotting.
void calculate_and_get_plot_data(
    double* a_in,      // Input: Pointer to array with A's coordinates [ax, ay]
    double* b_in,      // Input: Pointer to array with B's coordinates [bx, by]
    double* p_out,     // Output: Pointer to array to store P's coordinates [px, py]
    double* ratio_out, // Output: Pointer to array to store the ratio [m, n]
    double* line_x,    // Output: Array for the dividing line's x-coords
    double* line_y,    // Output: Array for the dividing line's y-coords
    int num_line_points) {

    // Extract input coordinates for easier use
    double ax = a_in[0];
    double ay = a_in[1];
    double bx = b_in[0];
    double by = b_in[1];

    // --- 1. Calculate the intersection point P ---
    // The line through A and B is: (y - ay) / (x - ax) = (by - ay) / (bx - ax)
    // The dividing line is: x - 3y = 0  => x = 3y
    // We solve the system of these two linear equations.
    double dx = bx - ax;
    double dy = by - ay;
    
    // Denominator for solving the system of equations
    double denominator = 3 * dy - dx;

    if (fabs(denominator) < 1e-9) {
        // The line AB is parallel to x - 3y = 0, no unique intersection.
        // We'll set P to (0,0) and ratio to 0:0 as a failure indicator.
        p_out[0] = 0;
        p_out[1] = 0;
        ratio_out[0] = 0;
        ratio_out[1] = 0;
        return;
    }

    // Calculate P's coordinates
    p_out[1] = (ax * dy - ay * dx) / denominator; // This is p_y
    p_out[0] = 3 * p_out[1];                     // This is p_x

    // --- 2. Calculate the ratio m:n ---
    // The ratio is the ratio of the lengths of the vectors AP and PB.
    double len_AP = sqrt(pow(p_out[0] - ax, 2) + pow(p_out[1] - ay, 2));
    double len_PB = sqrt(pow(bx - p_out[0], 2) + pow(by - p_out[1], 2));
    
    ratio_out[0] = len_AP;
    ratio_out[1] = len_PB;

    // --- 3. Generate points for the dividing line y = x/3 ---
    // Generate points around the segment AB for a nice plot
    double x_min = fmin(ax, bx) - 2.0;
    double x_max = fmax(ax, bx) + 2.0;
    double step = (x_max - x_min) / (num_line_points - 1);

    for (int i = 0; i < num_line_points; ++i) {
        line_x[i] = x_min + i * step;
        line_y[i] = line_x[i] / 3.0;
    }
}
