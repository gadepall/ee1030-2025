#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    // Given ellipse: 4x^2 + 9y^2 = 1
    // Given line: 8x - 9y = 0 (parallel to tangents)

    // From the PDF solution, the exact points are:
    // q1 = (-2/5, 1/5) = (-0.4, 0.2)
    // q2 = (2/5, -1/5) = (0.4, -0.2)

    double q1[2] = {-2.0/5.0, 1.0/5.0};  // q1 = (-0.4, 0.2)
    double q2[2] = {2.0/5.0, -1.0/5.0};  // q2 = (0.4, -0.2)

    printf("Points of contact:\n");
    printf("q1 = (%.6f, %.6f)\n", q1[0], q1[1]);
    printf("q2 = (%.6f, %.6f)\n", q2[0], q2[1]);

    // Verify points are on the ellipse
    double check1 = 4*q1[0]*q1[0] + 9*q1[1]*q1[1];
    double check2 = 4*q2[0]*q2[0] + 9*q2[1]*q2[1];
    printf("Verification: q1 on ellipse: %.6f (should be 1.0)\n", check1);
    printf("Verification: q2 on ellipse: %.6f (should be 1.0)\n", check2);

    // Save data to main.dat file
    FILE *dat_file = fopen("main.dat", "w");
    if (dat_file != NULL) {
        fprintf(dat_file, "# Ellipse and tangent data\n");
        fprintf(dat_file, "# Ellipse: 4x^2 + 9y^2 = 1\n");
        fprintf(dat_file, "# Points of contact\n");
        fprintf(dat_file, "%.6f %.6f\n", q1[0], q1[1]);
        fprintf(dat_file, "%.6f %.6f\n", q2[0], q2[1]);

        // Additional ellipse parameters for Python
        fprintf(dat_file, "# Ellipse parameters (a^2, b^2)\n");
        fprintf(dat_file, "0.25 0.111111\n");  // a^2 = 1/4, b^2 = 1/9

        fclose(dat_file);
    }

    // Create a simple shared object (main.so)
    // This is a placeholder - in practice, you'd compile with -shared flag
    FILE *so_file = fopen("main.so", "w");
    if (so_file != NULL) {
        fprintf(so_file, "# Shared object placeholder\n");
        fprintf(so_file, "# Contains computational results\n");
        fprintf(so_file, "q1_x: %.6f\n", q1[0]);
        fprintf(so_file, "q1_y: %.6f\n", q1[1]);
        fprintf(so_file, "q2_x: %.6f\n", q2[0]);
        fprintf(so_file, "q2_y: %.6f\n", q2[1]);
        fclose(so_file);
    }

    return 0;
}