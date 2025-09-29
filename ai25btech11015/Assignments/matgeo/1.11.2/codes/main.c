#include <stdio.h>
#include <math.h>

int main() {
    // Coordinates of P and Q
    double P[3] = {2, 1, -1};
    double Q[3] = {4, 4, -7};

    // Vector PQ = Q - P
    double PQ[3];
    for (int i = 0; i < 3; i++) {
        PQ[i] = Q[i] - P[i];
    }

    // Magnitude of PQ
    double magnitude = sqrt(PQ[0]*PQ[0] + PQ[1]*PQ[1] + PQ[2]*PQ[2]);

    // Unit vector along PQ
    double unit[3];
    for (int i = 0; i < 3; i++) {
        unit[i] = PQ[i] / magnitude;
    }

    // Print the unit vector
    printf("Unit vector along PQ: (%.4f, %.4f, %.4f)\n", unit[0], unit[1], unit[2]);
    // Write P, Q, and the unit vector to the file
    FILE *fp = fopen("unit_vector.dat", "w");
    if (fp != NULL) {
        fprintf(fp, "%.6f %.6f %.6f\n", P[0], P[1], P[2]);
        fprintf(fp, "%.6f %.6f %.6f\n", Q[0], Q[1], Q[2]);
        fprintf(fp, "%.6f %.6f %.6f\n", unit[0], unit[1], unit[2]);
        fclose(fp);
        printf("Coordinates written to unit_vector.dat\n");
    } else {
        printf("Error opening file for writing.\n");
    }

    return 0;
}