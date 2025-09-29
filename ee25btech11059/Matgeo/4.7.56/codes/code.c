#include <stdio.h>
#include <math.h>

// Function to compute line parameters
void compute_line_params(double m, double d, double* A, double* B, double* C1, double* C2) {
    // Normal vector to the line: n = (-m, 1)
    *A = -m;
    *B = 1.0;

    // Magnitude of the normal vector ||n||
    double norm = sqrt((*A) * (*A) + (*B) * (*B));

    // |c| = d * ||n||
    double abs_c = d * norm;

    // Return both +c and -c
    *C1 = abs_c;
    *C2 = -abs_c;
}

int main() {
    double m = -2.0 - sqrt(3.0);  // Given slope
    double d = 4.0;               // Perpendicular distance from origin

    double A, B, C1, C2;

    // Compute parameters
    compute_line_params(m, d, &A, &B, &C1, &C2);

    // Display the results
    printf("Equation of the lines:\n");
    printf("%.4fx + %.4fy = %.4f\n", A, B, C1);
    printf("%.4fx + %.4fy = %.4f\n", A, B, C2);

    return 0;
}
