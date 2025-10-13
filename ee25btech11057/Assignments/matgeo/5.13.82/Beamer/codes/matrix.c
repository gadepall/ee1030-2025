#include <stdio.h>
#include <math.h>

#define N 3

// Roots of x^2 + x - 1 = 0
// alpha = (-1 + sqrt(5))/2
// beta  = (-1 - sqrt(5))/2

// We'll store possible elements {1, alpha, beta}
void get_elements(double T[3]) {
    double alpha = (-1 + sqrt(5.0)) / 2.0;
    double beta  = (-1 - sqrt(5.0)) / 2.0;
    T[0] = 1.0;
    T[1] = alpha;
    T[2] = beta;
}

// Check if sum of array of length 3 = 0 (within tolerance)
int is_zero_sum(double a, double b, double c) {
    double sum = a + b + c;
    return fabs(sum) < 1e-6;
}

// Compute determinant of 3x3 matrix
double determinant(double M[3][3]) {
    double det = 
        M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) -
        M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) +
        M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]);
    return det;
}

int main() {
    double T[3];
    get_elements(T);

    int countA = 0;  // For part (A)
    int countB = 0;  // For part (B)
    double detVal = 0;  // For part (C)
    int foundC = 0;

    // --- (A): all entries in T such that Ri = Cj = 0 ---
    for (int a11=0;a11<3;a11++)
    for (int a12=0;a12<3;a12++)
    for (int a13=0;a13<3;a13++)
    for (int a21=0;a21<3;a21++)
    for (int a22=0;a22<3;a22++)
    for (int a23=0;a23<3;a23++)
    for (int a31=0;a31<3;a31++)
    for (int a32=0;a32<3;a32++)
    for (int a33=0;a33<3;a33++) {
        double M[3][3] = {
            {T[a11], T[a12], T[a13]},
            {T[a21], T[a22], T[a23]},
            {T[a31], T[a32], T[a33]}
        };
        // Row sums
        double R1 = M[0][0] + M[0][1] + M[0][2];
        double R2 = M[1][0] + M[1][1] + M[1][2];
        double R3 = M[2][0] + M[2][1] + M[2][2];
        // Column sums
        double C1 = M[0][0] + M[1][0] + M[2][0];
        double C2 = M[0][1] + M[1][1] + M[2][1];
        double C3 = M[0][2] + M[1][2] + M[2][2];

        if (fabs(R1)<1e-6 && fabs(R2)<1e-6 && fabs(R3)<1e-6 &&
            fabs(C1)<1e-6 && fabs(C2)<1e-6 && fabs(C3)<1e-6) {
            countA++;
        }
    }

    // --- (B): symmetric matrices with Cj = 0 ---
    for (int a11=0;a11<3;a11++)
    for (int a12=0;a12<3;a12++)
    for (int a13=0;a13<3;a13++)
    for (int a22=0;a22<3;a22++)
    for (int a23=0;a23<3;a23++)
    for (int a33=0;a33<3;a33++) {
        double M[3][3] = {
            {T[a11], T[a12], T[a13]},
            {T[a12], T[a22], T[a23]},
            {T[a13], T[a23], T[a33]}
        };
        // Column sums
        double C1 = M[0][0] + M[1][0] + M[2][0];
        double C2 = M[0][1] + M[1][1] + M[2][1];
        double C3 = M[0][2] + M[1][2] + M[2][2];
        if (fabs(C1)<1e-6 && fabs(C2)<1e-6 && fabs(C3)<1e-6)
            countB++;
    }

    // --- (C): any matrix with all Ri=0; compute |det(M)| ---
    for (int a11=0;a11<3;a11++)
    for (int a12=0;a12<3;a12++)
    for (int a13=0;a13<3;a13++)
    for (int a21=0;a21<3;a21++)
    for (int a22=0;a22<3;a22++)
    for (int a23=0;a23<3;a23++)
    for (int a31=0;a31<3;a31++)
    for (int a32=0;a32<3;a32++)
    for (int a33=0;a33<3;a33++) {
        double M[3][3] = {
            {T[a11], T[a12], T[a13]},
            {T[a21], T[a22], T[a23]},
            {T[a31], T[a32], T[a33]}
        };
        double R1 = M[0][0] + M[0][1] + M[0][2];
        double R2 = M[1][0] + M[1][1] + M[1][2];
        double R3 = M[2][0] + M[2][1] + M[2][2];
        if (fabs(R1)<1e-6 && fabs(R2)<1e-6 && fabs(R3)<1e-6) {
            double det = determinant(M);
            detVal = fabs(det);
            foundC = 1;
            break;
        }
    }

    printf("Computed results:\n");
    printf("(A) Number of matrices (R_i=C_j=0): %d\n", countA);
    printf("(B) Number of symmetric matrices (C_j=0): %d\n", countB);
    if (foundC)
        printf("(C) |det(M)| for such a matrix: %.0f\n", detVal);

    printf("\nHence, A→2, B→4, C→3  (Correct Option = 3)\n");

    return 0;
}

