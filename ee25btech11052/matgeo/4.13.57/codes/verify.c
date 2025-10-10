#include <math.h>

// Calculates the distance between two points (x1, y1) and (x2, y2)
double distance(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

// Main function to be called from Python
// It calculates the intercept length of a line (sol_A*x + sol_B*y = sol_C)
// between two parallel lines (p1_A*x + p1_B*y = p1_C) and (p2_A*x + p2_B*y = p2_C).
double calculate_intercept_length(
    double sol_A, double sol_B, double sol_C,
    double p1_A, double p1_B, double p1_C,
    double p2_A, double p2_B, double p2_C
) {
    // Solve for the intersection of the solution line with the first parallel line
    // sol_A*x + sol_B*y = sol_C
    // p1_A*x + p1_B*y = p1_C
    // Using Cramer's rule for simplicity
    double det = sol_A * p1_B - p1_A * sol_B;
    if (fabs(det) < 1e-9) return -1.0; // Lines are parallel, no unique intersection
    
    double x1 = (p1_B * sol_C - sol_B * p1_C) / det;
    double y1 = (sol_A * p1_C - p1_A * sol_C) / det;

    // Solve for the intersection of the solution line with the second parallel line
    // sol_A*x + sol_B*y = sol_C
    // p2_A*x + p2_B*y = p2_C
    det = sol_A * p2_B - p2_A * sol_B;
    if (fabs(det) < 1e-9) return -1.0; // Should be the same determinant

    double x2 = (p2_B * sol_C - sol_B * p2_C) / det;
    double y2 = (sol_A * p2_C - p2_A * sol_C) / det;

    // Return the distance between the two intersection points
    return distance(x1, y1, x2, y2);
}
