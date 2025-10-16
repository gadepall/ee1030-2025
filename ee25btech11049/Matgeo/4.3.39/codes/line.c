#include <stdio.h>

// Function to generate points on a line segment between A and B.
// P(lambda) = A + lambda * (B - A)
//
// Parameters:
//   Ax, Ay: Coordinates of the starting point A.
//   Bx, By: Coordinates of the end point B.
//   num_points: The number of points to generate for the line.
//   out_x: A pointer to an array to store the generated x-coordinates.
//   out_y: A pointer to an array to store the generated y-coordinates.
void generate_line_points(double Ax, double Ay, double Bx, double By, int num_points, double* out_x, double* out_y) {
    // Calculate the direction vector m = B - A
    double mx = Bx - Ax;
    double my = By - Ay;

    // Generate 'num_points' by varying lambda from 0.0 to 1.0
    for (int i = 0; i < num_points; i++) {
        // Calculate lambda, ensuring it spans from 0 to 1 inclusive
        double lambda = (double)i / (num_points - 1);

        // Calculate the point P using the parametric equation
        // P_x = A_x + lambda * m_x
        // P_y = A_y + lambda * m_y
        out_x[i] = Ax + lambda * mx;
        out_y[i] = Ay + lambda * my;
    }
}

