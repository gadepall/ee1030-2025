#include <math.h>

/*
 * This function calculates the coordinates of the two points of contact.
 *
 * @param radius: The radius of the circle.
 * @param p_x: The x-coordinate of the external point P.
 * @param out_q1_x, out_q1_y: Pointers to store the coordinates of the first contact point.
 * @param out_q2_x, out_q2_y: Pointers to store the coordinates of the second contact point.
 * @return: 0 on success, -1 on error (e.g., point is inside the circle).
 */
int calculate_tangent_points(double radius, double p_x, 
                             double *out_q1_x, double *out_q1_y,
                             double *out_q2_x, double *out_q2_y) {
    
    // Based on the condition: p_x * q_x = radius^2
    // For this specific problem, it was 6 * q_x = 16
    double q_x = (radius * radius) / p_x;

    // Based on the condition: q_x^2 + q_y^2 = radius^2
    double q_y_squared = (radius * radius) - (q_x * q_x);
    
    // Check if the point is inside the circle (no real tangents)
    if (q_y_squared < 0) {
        return -1; // Error code
    }

    double q_y = sqrt(q_y_squared);

    // Assign the coordinates to the output pointers
    *out_q1_x = q_x;
    *out_q1_y = q_y;
    
    *out_q2_x = q_x;
    *out_q2_y = -q_y;

    return 0; // Success
}