#include <stdio.h>
#include <stdlib.h>
#include "geofun.h"
#include "matfun.h"
#include <math.h>

// Helper function for dot product of two 3D vectors
double dot_product(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Helper function for Euclidean norm of a 3D vector
double norm(double v[3]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

int main() {
    // Solution for the given question

    // Plane 1: r·(2i - 3j + k) = 1
    // Normal vector n1 = (2, -3, 1), equation: 2x - 3y + z = 1
    double n1[3] = {2, -3, 1}, d1 = 1;

    // Plane 2: r·(i - j) = 4
    // Normal vector n2 = (1, -1, 0), equation: x - y = 4
    double n2[3] = {1, -1, 0}, d2 = 4;

    // Compute dot product and norms
    double dp = dot_product(n1, n2);
    double norm1 = norm(n1);
    double norm2 = norm(n2);

    // Cosine of the angle between the planes
    double cos_theta = dp / (norm1 * norm2);

    // Print solution details
    printf("Plane 1 Equation: 2x - 3y + z = 1\n");
    printf("Normal Vector 1: (2, -3, 1)\n");
    printf("Plane 2 Equation: x - y = 4\n");
    printf("Normal Vector 2: (1, -1, 0)\n");
    printf("Dot Product n1·n2 = %.2f\n", dp);
    printf("Norm |n1| = %.2f, Norm |n2| = %.2f\n", norm1, norm2);
    printf("Cosine of angle between planes: %.5f\n", cos_theta);

    // Write plane coefficients and cos(theta) to output.dat
    // Format: n1_x n1_y n1_z d1 n2_x n2_y n2_z d2 cos_theta
    FILE *fp = fopen("output.dat", "w");
    if (!fp) {
        printf("Error opening output.dat\n");
        return 1;
    }
    fprintf(fp, "%lf %lf %lf %lf %lf %lf %lf %lf %lf\n",
            n1[0], n1[1], n1[2], d1,
            n2[0], n2[1], n2[2], d2,
            cos_theta);
    fclose(fp);

    printf("All results saved to output.dat for plotting in Python.\n");
    return 0;
}
