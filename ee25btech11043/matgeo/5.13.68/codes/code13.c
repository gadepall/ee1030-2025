#include <stdio.h>

// Function to calculate the determinant of the 3x3 matrix
// | 1  k   3 |
// | 3  k  -2 |
// | 2  3  -4 |
double calculateDeterminant(double k_val) {
    double det = 0.0;
    det = (1.0 * (k_val * -4.0 - (-2.0 * 3.0))) -
          (k_val * (3.0 * -4.0 - (-2.0 * 2.0))) +
          (3.0 * (3.0 * 3.0 - k_val * 2.0));
    return det;
}

// Function to solve the system for a given k when det = 0
// It will express x, y in terms of z
// This function assumes a non-trivial solution exists (det = 0)
// For k = 33/2 (16.5):
// x + 16.5y + 3z = 0
// 3x + 16.5y - 2z = 0
// 2x + 3y - 4z = 0
// Subtracting (Eq1) from (Eq2):
// (3x - x) + (16.5y - 16.5y) + (-2z - 3z) = 0 - 0
// 2x - 5z = 0  =>  2x = 5z  =>  x = 5/2 * z
//
// Substitute x = 5/2 * z into (Eq3):
// 2 * (5/2 * z) + 3y - 4z = 0
// 5z + 3y - 4z = 0
// z + 3y = 0  =>  3y = -z  =>  y = -1/3 * z
//
// So, the solutions are of the form (5/2 * z, -1/3 * z, z) for any rational z.
void solveSystem(double k_val, double* x_coeff_z, double* y_coeff_z) {
    if (k_val == 33.0 / 2.0) { // Check if k is the correct value
        *x_coeff_z = 5.0 / 2.0;
        *y_coeff_z = -1.0 / 3.0;
    } else {
        // Handle cases where k is not the value that makes det=0,
        *x_coeff_z = 0.0;
        *y_coeff_z = 0.0;
    }
}