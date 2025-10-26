#include <math.h>

// Define PI if not already defined (e.g., on some compilers)
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

/**
 * @brief Calculates the coordinates for plotting two circles and a tangent line.
 * * This function calculates the (x, y) points for two distinct circles and one of their
 * common tangent lines based on predefined geometric properties. The points are
 * generated using parametric equations.
 * * @param x1 Pointer to an array to store the x-coordinates of the first circle.
 * @param y1 Pointer to an array to store the y-coordinates of the first circle.
 * @param x2 Pointer to an array to store the x-coordinates of the second circle.
 * @param y2 Pointer to an array to store the y-coordinates of the second circle.
 * @param x_tangent2 Pointer to an array to store the x-coordinates for the second tangent line.
 * @param y_tangent2 Pointer to an array to store the y-coordinates for the second tangent line.
 * @param num_points The number of points to generate for each curve, determining the resolution.
 */
void calculate_plot_data(double* x1, double* y1, double* x2, double* y2, 
                         double* x_tangent2, double* y_tangent2, int num_points) {
    // Circle 1: Center (2, 1), Radius 1.0
    const double c1_center_x = 2.0;
    const double c1_center_y = 1.0;
    const double c1_radius = 1.0;

    // Circle 2: Center (6, 4), Radius 4.0
    const double c2_center_x = 6.0;
    const double c2_center_y = 4.0;
    const double c2_radius = 4.0;
    
    // Range for the tangent line plot
    const double tangent_x_start = -1.0;
    const double tangent_x_end = 9.0;
    const double tangent_x_range = tangent_x_end - tangent_x_start;

    for (int i = 0; i < num_points; ++i) {
        // Calculate angle for circle parameterization
        double theta = 2.0 * M_PI * i / (num_points - 1);

        // Calculate points for Circle 1
        x1[i] = c1_center_x + c1_radius * cos(theta);
        y1[i] = c1_center_y + c1_radius * sin(theta);

        // Calculate points for Circle 2
        x2[i] = c2_center_x + c2_radius * cos(theta);
        y2[i] = c2_center_y + c2_radius * sin(theta);
        
        // Calculate points for Tangent 2: 24x - 7y - 16 = 0 => y = (24x - 16) / 7
        double current_x = tangent_x_start + (double)i * tangent_x_range / (num_points - 1);
        x_tangent2[i] = current_x;
        y_tangent2[i] = (24.0 * current_x - 16.0) / 7.0;
    }
}

/**
 * @brief Calculates the point of contact and tangent slopes for the two circles.
 * * This function computes the coordinates of the point where the two circles touch
 * and the slopes of their two common tangent lines based on the geometry derived
 * from the problem statement.
 * * @param p_x Pointer to a double to store the x-coordinate of the contact point.
 * @param p_y Pointer to a double to store the y-coordinate of the contact point.
 * @param m1 Pointer to a double to store the slope of the first tangent.
 * @param m2 Pointer to a double to store the slope of the second tangent.
 */
void calculate_geometric_properties(double* p_x, double* p_y, double* m1, double* m2) {
    // Circle 1: Center (2, 1), Radius 1.0
    const double c1_x = 2.0;
    const double c1_y = 1.0;
    const double r1 = 1.0;

    // Circle 2: Center (6, 4), Radius 4.0
    const double c2_x = 6.0;
    const double c2_y = 4.0;
    const double r2 = 4.0;

    // Calculate the point of contact (P) which divides the line segment 
    // connecting the centers c1 and c2 in the ratio r1:r2.
    *p_x = (c1_x * r2 + c2_x * r1) / (r1 + r2);
    *p_y = (c1_y * r2 + c2_y * r1) / (r1 + r2);

    // The slopes of the common tangents (m) are derived from solving
    // the distance from the center to the tangent line equation for both circles.
    // This leads to the quadratic equation: 7m^2 - 24m = 0, which gives m(7m - 24) = 0.
    *m1 = 0.0;
    *m2 = 24.0 / 7.0;
}
