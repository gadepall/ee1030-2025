// File: vector_ops.c

// This function verifies if a given vector 'b' is the correct solution.
// It returns 0 for success, or a non-zero code for failure.
int verify_solution(double a[3], double b[3], double target_dot, double target_cross[3]) {
    
    // Calculate the dot product: a . b
    double calculated_dot = a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

    // Calculate the cross product: a x b
    double calculated_cross[3];
    calculated_cross[0] = a[1] * b[2] - a[2] * b[1];
    calculated_cross[1] = a[2] * b[0] - a[0] * b[2];
    calculated_cross[2] = a[0] * b[1] - a[1] * b[0];

    // Check if the calculated values match the targets
    int dot_match = (calculated_dot == target_dot);
    int cross_match = (calculated_cross[0] == target_cross[0] &&
                       calculated_cross[1] == target_cross[1] &&
                       calculated_cross[2] == target_cross[2]);

    // Return the result code
    if (dot_match && cross_match) {
        return 0; // Success
    } else if (!dot_match && cross_match) {
        return 1; // Dot product failed
    } else if (dot_match && !cross_match) {
        return 2; // Cross product failed
    } else {
        return 3; // Both failed
    }
}