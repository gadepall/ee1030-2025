#include <math.h>
#include <stdio.h>

// Function to compute side lengths and angles using matrix (vector dot product) method
void triangle_properties(double *sides, double *angles) {
    // Vertices: A(-4,0), B(0,3), C(4,0)
    double A[2] = {-4, 0};
    double B[2] = {0, 3};
    double C[2] = {4, 0};

    // --- Compute side vectors ---
    double AB[2] = {B[0] - A[0], B[1] - A[1]};
    double BC[2] = {C[0] - B[0], C[1] - B[1]};
    double CA[2] = {A[0] - C[0], A[1] - C[1]};

    // --- Compute side lengths using dot product (matrix method) ---
    sides[0] = sqrt(AB[0]*AB[0] + AB[1]*AB[1]); // AB
    sides[1] = sqrt(BC[0]*BC[0] + BC[1]*BC[1]); // BC
    sides[2] = sqrt(CA[0]*CA[0] + CA[1]*CA[1]); // CA

    // --- Compute angles using dot product ---
    // ∠A = angle between AB and AC
    double AC[2] = {C[0] - A[0], C[1] - A[1]};
    double dot_A = AB[0]*AC[0] + AB[1]*AC[1];
    double norm_AB = sqrt(AB[0]*AB[0] + AB[1]*AB[1]);
    double norm_AC = sqrt(AC[0]*AC[0] + AC[1]*AC[1]);
    angles[0] = acos(dot_A / (norm_AB * norm_AC)) * 180.0 / M_PI;

    // ∠B = angle between BA and BC
    double BA[2] = {A[0] - B[0], A[1] - B[1]};
    double dot_B = BA[0]*BC[0] + BA[1]*BC[1];
    double norm_BA = sqrt(BA[0]*BA[0] + BA[1]*BA[1]);
    double norm_BC = sqrt(BC[0]*BC[0] + BC[1]*BC[1]);
    angles[1] = acos(dot_B / (norm_BA * norm_BC)) * 180.0 / M_PI;

    // ∠C = angle between CA and CB
    double CB[2] = {B[0] - C[0], B[1] - C[1]};
    double dot_C = CA[0]*CB[0] + CA[1]*CB[1];
    double norm_CA = sqrt(CA[0]*CA[0] + CA[1]*CA[1]);
    double norm_CB = sqrt(CB[0]*CB[0] + CB[1]*CB[1]);
    angles[2] = acos(dot_C / (norm_CA * norm_CB)) * 180.0 / M_PI;
}
