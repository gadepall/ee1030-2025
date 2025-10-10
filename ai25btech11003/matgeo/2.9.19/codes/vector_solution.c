#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/geofun.h"
#include "libs/matfun.h"

// Function to save vectors to file
void saveVectorsToFile(double **a, double **b, double **c, double **result, const char *filename) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }
    
    fprintf(fp, "# Vector data for the problem\n");
    fprintf(fp, "# Format: vector_name x y z\n");
    fprintf(fp, "a %.6f %.6f %.6f\n", a[0][0], a[1][0], a[2][0]);
    fprintf(fp, "b %.6f %.6f %.6f\n", b[0][0], b[1][0], b[2][0]);
    fprintf(fp, "c %.6f %.6f %.6f\n", c[0][0], c[1][0], c[2][0]);
    fprintf(fp, "result %.6f %.6f %.6f\n", result[0][0], result[1][0], result[2][0]);
    fprintf(fp, "# Magnitude of result vector: %.6f\n", Matnorm(result, 3));
    
    fclose(fp);
}

// Function to compute 3a - 2b + 2c
double **computeResult(double **a, double **b, double **c) {
    double **scaled_a = Matscale(a, 3, 1, 3.0);
    double **scaled_b = Matscale(b, 3, 1, -2.0);
    double **scaled_c = Matscale(c, 3, 1, 2.0);
    
    double **temp = Matadd(scaled_a, scaled_b, 3, 1);
    double **result = Matadd(temp, scaled_c, 3, 1);
    
    freeMat(scaled_a, 3);
    freeMat(scaled_b, 3);
    freeMat(scaled_c, 3);
    freeMat(temp, 3);
    
    return result;
}

// Function exported for Python to use
double compute_vector_magnitude(double *a, double *b, double *c) {
    // Create matrix representations
    double **vec_a = createMat(3, 1);
    double **vec_b = createMat(3, 1);
    double **vec_c = createMat(3, 1);
    
    for (int i = 0; i < 3; i++) {
        vec_a[i][0] = a[i];
        vec_b[i][0] = b[i];
        vec_c[i][0] = c[i];
    }
    
    double **result = computeResult(vec_a, vec_b, vec_c);
    double magnitude = Matnorm(result, 3);
    
    freeMat(vec_a, 3);
    freeMat(vec_b, 3);
    freeMat(vec_c, 3);
    freeMat(result, 3);
    
    return magnitude;
}

int main() {
    printf("Solving: Find |3a - 2b + 2c| where |a|=1, |b|=2, |c|=3\n");
    printf("Conditions: proj_a(b) = proj_a(c) and b ⊥ c\n\n");
    
    // Create specific vectors that satisfy the given conditions
    // Let a = (1, 0, 0) - unit vector along x-axis
    double **a = createMat(3, 1);
    a[0][0] = 1.0; a[1][0] = 0.0; a[2][0] = 0.0;
    
    // For b and c to have equal projections along a and be perpendicular:
    // b·a = c·a and b·c = 0
    // Choose vectors that satisfy these conditions properly:
    
    double k = 0.5; // projection value
    
    // b = (k, sqrt(4-k²), 0)
    double **b = createMat(3, 1);
    b[0][0] = k;
    b[1][0] = sqrt(4 - k*k);
    b[2][0] = 0.0;
    
    // c = (k, m, n) where b·c = 0 and |c| = 3
    // From b·c = 0: k*k + m*sqrt(4-k²) = 0
    // So m = -k*k/sqrt(4-k²)
    double **c = createMat(3, 1);
    c[0][0] = k;
    c[1][0] = -k*k / sqrt(4 - k*k);
    
    // n² = 9 - k² - m²
    double m = c[1][0];
    double n_squared = 9 - k*k - m*m;
    c[2][0] = sqrt(n_squared);
    
    printf("Vector a: ");
    printMat(a, 3, 1);
    printf("Magnitude of a: %.6f\n\n", Matnorm(a, 3));
    
    printf("Vector b: ");
    printMat(b, 3, 1);
    printf("Magnitude of b: %.6f\n\n", Matnorm(b, 3));
    
    printf("Vector c: ");
    printMat(c, 3, 1);
    printf("Magnitude of c: %.6f\n\n", Matnorm(c, 3));
    
    // Verify conditions
    printf("Verification of conditions:\n");
    printf("b·a = %.6f\n", Matdot(b, a, 3));
    printf("c·a = %.6f\n", Matdot(c, a, 3));
    printf("b·c = %.6f\n", Matdot(b, c, 3));
    printf("Equal projections: %s\n", (fabs(Matdot(b, a, 3) - Matdot(c, a, 3)) < 1e-10) ? "Yes" : "No");
    printf("Perpendicular: %s\n", (fabs(Matdot(b, c, 3)) < 1e-10) ? "Yes" : "No");
    printf("\n");
    
    // Compute 3a - 2b + 2c
    double **result = computeResult(a, b, c);
    
    printf("Result vector (3a - 2b + 2c): ");
    printMat(result, 3, 1);
    
    double magnitude = Matnorm(result, 3);
    printf("Magnitude |3a - 2b + 2c| = %.6f\n", magnitude);
    printf("Theoretical value = sqrt(61) = %.6f\n", sqrt(61));
    printf("Error: %.10f\n\n", fabs(magnitude - sqrt(61)));
    
    // Save vectors to file
    saveVectorsToFile(a, b, c, result, "vectors.dat");
    printf("Vectors saved to vectors.dat\n");
    
    // Clean up
    freeMat(a, 3);
    freeMat(b, 3);
    freeMat(c, 3);
    freeMat(result, 3);
    
    return 0;
}