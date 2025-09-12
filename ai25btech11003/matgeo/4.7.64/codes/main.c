#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to solve 3x3 system using Gaussian elimination
void solve_system(double A[3][4], double *n) {
    int i, j, k;
    double factor;

    // Forward elimination
    for (i = 0; i < 3; i++) {
        // Find pivot
        int max_row = i;
        for (k = i + 1; k < 3; k++) {
            if (fabs(A[k][i]) > fabs(A[max_row][i])) {
                max_row = k;
            }
        }

        // Swap rows
        if (max_row != i) {
            for (j = 0; j < 4; j++) {
                double temp = A[i][j];
                A[i][j] = A[max_row][j];
                A[max_row][j] = temp;
            }
        }

        // Make all rows below this one 0 in current column
        for (k = i + 1; k < 3; k++) {
            if (A[i][i] != 0) {
                factor = A[k][i] / A[i][i];
                for (j = i; j < 4; j++) {
                    A[k][j] -= factor * A[i][j];
                }
            }
        }
    }

    // Back substitution
    for (i = 2; i >= 0; i--) {
        n[i] = A[i][3];
        for (j = i + 1; j < 3; j++) {
            n[i] -= A[i][j] * n[j];
        }
        if (A[i][i] != 0) {
            n[i] /= A[i][i];
        }
    }
}

// Function to calculate normal vector of plane given three points
void find_plane_normal(double A[3], double B[3], double C[3], double *n) {
    // Set up the system of equations: A^T * n = 1
    double system[3][4] = {
        {A[0], A[1], A[2], 1.0},
        {B[0], B[1], B[2], 1.0},
        {C[0], C[1], C[2], 1.0}
    };

    solve_system(system, n);
}

// Function to calculate distance from point to plane
double point_to_plane_distance(double P[3], double n[3]) {
    // Calculate n^T * P - 1
    double dot_product = n[0] * P[0] + n[1] * P[1] + n[2] * P[2];
    double numerator = fabs(dot_product - 1.0);

    // Calculate ||n||
    double norm = sqrt(n[0] * n[0] + n[1] * n[1] + n[2] * n[2]);

    return numerator / norm;
}

// Function to calculate vector norm
double vector_norm(double v[3]) {
    return sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
}

// Function to calculate dot product
double dot_product_func(double a[3], double b[3]) {
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

// Function to write vectors to .dat file
void write_vectors_to_file(const char* filename, double A[3], double B[3], double C[3], double P[3], double n[3]) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error: Unable to create %s\n", filename);
        return;
    }

    fprintf(file, "# Vector data for distance between point and plane problem\n");
    fprintf(file, "# Point A\n");
    fprintf(file, "A %.0f %.0f %.0f\n", A[0], A[1], A[2]);
    fprintf(file, "# Point B\n");
    fprintf(file, "B %.0f %.0f %.0f\n", B[0], B[1], B[2]);
    fprintf(file, "# Point C\n");
    fprintf(file, "C %.0f %.0f %.0f\n", C[0], C[1], C[2]);
    fprintf(file, "# Point P\n");
    fprintf(file, "P %.0f %.0f %.0f\n", P[0], P[1], P[2]);
    fprintf(file, "# Normal vector n\n");
    fprintf(file, "n %.10f %.10f %.10f\n", n[0], n[1], n[2]);

    fclose(file);
    printf("vectors.dat file created successfully.\n");
}

int main() {
    printf("=== Distance Between Point and Plane Solution ===\n\n");

    // Define points A, B, C, P as per the problem
    double A[3] = {3.0, -1.0, 2.0};
    double B[3] = {5.0, 2.0, 4.0};
    double C[3] = {-1.0, -1.0, 6.0};
    double P[3] = {6.0, 5.0, 9.0};

    printf("Points from the problem:\n");
    printf("A = (%.0f, %.0f, %.0f)\n", A[0], A[1], A[2]);
    printf("B = (%.0f, %.0f, %.0f)\n", B[0], B[1], B[2]);
    printf("C = (%.0f, %.0f, %.0f)\n", C[0], C[1], C[2]);
    printf("P = (%.0f, %.0f, %.0f)\n\n", P[0], P[1], P[2]);

    // Calculate normal vector n
    double n[3];
    find_plane_normal(A, B, C, n);

    printf("Solution:\n");
    printf("Normal vector n = (%.10f, %.10f, %.10f)\n", n[0], n[1], n[2]);

    // Calculate distance
    double distance = point_to_plane_distance(P, n);
    printf("Distance from point P to plane = %.10f units\n\n", distance);

    // Manual calculation as per PDF: d = |n^T*P - 1| / ||n||
    double manual_numerator = fabs((18.0 - 20.0 + 27.0)/19.0 - 1.0);
    double manual_denominator = sqrt(34.0)/19.0;
    double manual_distance = manual_numerator / manual_denominator;
    double expected_distance = 3.0 * sqrt(34.0) / 17.0;

    // Write all vectors to vectors.dat file
    write_vectors_to_file("vectors.dat", A, B, C, P, n);

    return 0;
}
