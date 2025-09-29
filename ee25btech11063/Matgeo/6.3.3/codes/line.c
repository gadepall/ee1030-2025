#include <stdio.h>
#include <math.h>

int main() {
    // Define P1, d1, P2, d2
    double P1[3] = {8, -9, 10};
    double d1[3] = {3, -16, 7};
    double P2[3] = {15, 29, 5};
    double d2[3] = {3, 8, -5};

    // Compute c = P1 - P2
    double c[3];
    for (int i = 0; i < 3; i++) {
        c[i] = P1[i] - P2[i];
    }

    // Matrix M = [d1  -d2]
    double M[3][2] = {
        { d1[0], -d2[0] },
        { d1[1], -d2[1] },
        { d1[2], -d2[2] }
    };

    // Compute M^T * M (2x2 matrix)
    double MTM[2][2] = {0};
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 3; k++) {
                MTM[i][j] += M[k][i] * M[k][j];
            }
        }
    }

    // Compute -M^T * c (2x1 vector)
    double rhs[2] = {0};
    for (int i = 0; i < 2; i++) {
        for (int k = 0; k < 3; k++) {
            rhs[i] -= M[k][i] * c[k];
        }
    }

    // Solve 2x2 linear system MTM * x = rhs
    double det = MTM[0][0]*MTM[1][1] - MTM[0][1]*MTM[1][0];
    double lambda = ( rhs[0]*MTM[1][1] - rhs[1]*MTM[0][1] ) / det;
    double mu     = ( MTM[0][0]*rhs[1] - MTM[1][0]*rhs[0] ) / det;

    // Closest points Q1 and Q2
    double Q1[3], Q2[3];
    for (int i = 0; i < 3; i++) {
        Q1[i] = P1[i] + lambda * d1[i];
        Q2[i] = P2[i] + mu * d2[i];
    }

    // Distance = ||Q1 - Q2||
    double dx = Q1[0] - Q2[0];
    double dy = Q1[1] - Q2[1];
    double dz = Q1[2] - Q2[2];
    double distance = sqrt(dx*dx + dy*dy + dz*dz);

    // Write result to file "line.dat"
    FILE *fp = fopen("line.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(fp, "Shortest distance between the lines = %.2f\n", distance);
    fclose(fp);

    return 0;
}

