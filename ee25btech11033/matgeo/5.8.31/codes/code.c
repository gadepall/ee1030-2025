void calculate_angles(double* angle_A, double* angle_B, double* angle_C) {
    // The system of equations can be simplified to express everything in terms of A:
    // From (3): 3B = 2A + 2B  =>  B = 2A
    // Substitute B into (2): C = 3 * (2A)  =>  C = 6A
    // Substitute B and C into (1): A + 2A + 6A = 180  =>  9A = 180

    // Now, we solve this simplified system using code:

    // First, solve for angle A from the equation 9A = 180
    *angle_A = 180.0 / 9.0;

    // Next, calculate angle B using the relationship B = 2A
    *angle_B = 2.0 * (*angle_A);

    // Finally, calculate angle C using the relationship C = 3B (or C = 6A)
    *angle_C = 3.0 * (*angle_B);
}