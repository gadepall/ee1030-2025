#include <stdio.h>

int main() {
    // Define vector b
    double b[2] = {4.0, 3.0};
    
    // Vector c perpendicular to b: c = (-b_y, b_x)
    double c[2] = {-b[1], b[0]};
    
    // Scalar projections
    double proj_b = 5.0;   // r^T b = 5
    double proj_c = 10.0;  // r^T c = 10

    // Solve 2x2 system using determinant (Cramer's rule)
    double det = b[0]*c[1] - b[1]*c[0];
    double r1 = (proj_b*c[1] - b[1]*proj_c)/det;
    double r2 = (b[0]*proj_c - proj_b*c[0])/det;

    // Print results
    printf("Vector b = (%.1f, %.1f)\n", b[0], b[1]);
    printf("Vector c = (%.1f, %.1f) (perpendicular to b)\n", c[0], c[1]);
    printf("Scalar projection on b = %.1f\n", proj_b);
    printf("Scalar projection on c = %.1f\n", proj_c);
    printf("Required vector r = (%.6f, %.6f)\n", r1, r2);

    // Write results to dat file
    FILE *file = fopen("vector_solution.dat", "w");
    if(file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "b_x\tb_y\tc_x\tc_y\tproj_b\tproj_c\tr1\tr2\n");
    fprintf(file, "%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.6f\t%.6f\n",
            b[0], b[1], c[0], c[1], proj_b, proj_c, r1, r2);

    fclose(file);
    printf("Results written to values.dat\n");

    return 0;
}

