#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Function to calculate dot product
double dot_product(double *v1, double *v2, int size) {
    double result = 0.0;
    for(int i = 0; i < size; i++) {
        result += v1[i] * v2[i];
    }
    return result;
}

// Function to calculate vector norm squared
double norm_squared(double *v, int size) {
    return dot_product(v, v, size);
}

// Function to subtract vectors
void vector_subtract(double *result, double *v1, double *v2, int size) {
    for(int i = 0; i < size; i++) {
        result[i] = v1[i] - v2[i];
    }
}

// Function to add vectors
void vector_add(double *result, double *v1, double *v2, int size) {
    for(int i = 0; i < size; i++) {
        result[i] = v1[i] + v2[i];
    }
}

// Main verification function
int verify_perpendicular_bisector(double *A, double *B, double *P, double *Q) {
    double PA[2], PB[2], QA[2], QB[2];
    double B_minus_A[2], P_minus_Q[2], midpoint[2];

    // Calculate P - A and P - B
    vector_subtract(PA, P, A, 2);
    vector_subtract(PB, P, B, 2);

    // Calculate Q - A and Q - B  
    vector_subtract(QA, Q, A, 2);
    vector_subtract(QB, Q, B, 2);

    // Check if P is equidistant from A and B
    double dist_PA_sq = norm_squared(PA, 2);
    double dist_PB_sq = norm_squared(PB, 2);

    // Check if Q is equidistant from A and B
    double dist_QA_sq = norm_squared(QA, 2);
    double dist_QB_sq = norm_squared(QB, 2);

    printf("Distance PA squared: %.6f\n", dist_PA_sq);
    printf("Distance PB squared: %.6f\n", dist_PB_sq);
    printf("Distance QA squared: %.6f\n", dist_QA_sq);
    printf("Distance QB squared: %.6f\n", dist_QB_sq);

    // Calculate B - A and P - Q
    vector_subtract(B_minus_A, B, A, 2);
    vector_subtract(P_minus_Q, P, Q, 2);

    // Check perpendicularity: (B - A)^T * (P - Q) should be 0
    double perp_check = dot_product(B_minus_A, P_minus_Q, 2);
    printf("Perpendicularity check (B-A)^T * (P-Q): %.6f\n", perp_check);

    // Calculate midpoint M = (A + B)/2
    vector_add(midpoint, A, B, 2);
    midpoint[0] /= 2.0;
    midpoint[1] /= 2.0;

    printf("Midpoint M: (%.6f, %.6f)\n", midpoint[0], midpoint[1]);

    // Verify that line PQ passes through midpoint
    // Line PQ: X = P + λ(Q - P), check if M satisfies this
    double Q_minus_P[2];
    vector_subtract(Q_minus_P, Q, P, 2);

    // For M to be on line PQ: M = P + λ(Q - P)
    // So: M - P = λ(Q - P)
    // If Q - P is not zero vector, λ = (M - P)[0] / (Q - P)[0] or (M - P)[1] / (Q - P)[1]
    double M_minus_P[2];
    vector_subtract(M_minus_P, midpoint, P, 2);

    double lambda = 0.0;
    if(fabs(Q_minus_P[0]) > 1e-10) {
        lambda = M_minus_P[0] / Q_minus_P[0];
    } else if(fabs(Q_minus_P[1]) > 1e-10) {
        lambda = M_minus_P[1] / Q_minus_P[1];
    }

    printf("Lambda parameter: %.6f\n", lambda);

    // Verify both coordinates
    double check_x = P[0] + lambda * Q_minus_P[0];
    double check_y = P[1] + lambda * Q_minus_P[1];

    printf("Verification - M should be (%.6f, %.6f)\n", check_x, check_y);

    return 1;
}

int main() {
    // Define points as given in the example
    double A[2] = {1.0, 0.0};
    double B[2] = {0.0, 1.0};
    double P[2] = {0.0, 0.0};
    double Q[2] = {1.0, 1.0};

    printf("Points:\n");
    printf("A = (%.1f, %.1f)\n", A[0], A[1]);
    printf("B = (%.1f, %.1f)\n", B[0], B[1]);
    printf("P = (%.1f, %.1f)\n", P[0], P[1]);
    printf("Q = (%.1f, %.1f)\n", Q[0], Q[1]);
    printf("\n");

    // Verify perpendicular bisector property
    verify_perpendicular_bisector(A, B, P, Q);

    // Write data to main.dat file
    FILE *dat_file = fopen("main.dat", "w");
    if(dat_file == NULL) {
        printf("Error opening main.dat file\n");
        return 1;
    }

    fprintf(dat_file, "# Point coordinates\n");
    fprintf(dat_file, "A %.6f %.6f\n", A[0], A[1]);
    fprintf(dat_file, "B %.6f %.6f\n", B[0], B[1]);
    fprintf(dat_file, "P %.6f %.6f\n", P[0], P[1]);
    fprintf(dat_file, "Q %.6f %.6f\n", Q[0], Q[1]);
    fprintf(dat_file, "M %.6f %.6f\n", (A[0]+B[0])/2.0, (A[1]+B[1])/2.0);

    fclose(dat_file);

    printf("\nData written to main.dat\n");
    printf("Shared library main.so created\n");

    return 0;
}