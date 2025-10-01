#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    // Step 1: Line in vector form
    double P[3] = {2.0, -1.0, 2.0}; // point on line
    double d[3] = {1.0, 1.0, 1.0};  // direction vector

    // Step 2: Plane in vector form
    double n[3] = {2.0, 1.0, 1.0}; // normal vector
    double plane_constant = 9.0;    // n^T * r = 9

    // Step 3: Compute t for intersection
    double numerator = n[0]*P[0] + n[1]*P[1] + n[2]*P[2];   // n^T * P
    double denominator = n[0]*d[0] + n[1]*d[1] + n[2]*d[2]; // n^T * d
    double t = (plane_constant - numerator) / denominator;

    // Step 4: Compute intersection point Q = P + t*d
    double Q[3];
    for(int i=0; i<3; i++) {
        Q[i] = P[i] + t * d[i];
    }

    // Step 5: Compute vector PQ and its magnitude
    double PQ[3];
    for(int i=0; i<3; i++) {
        PQ[i] = Q[i] - P[i];
    }
    double PQ_length = sqrt(PQ[0]*PQ[0] + PQ[1]*PQ[1] + PQ[2]*PQ[2]);

    // Print results step by step
    printf("Step 1: Line in vector form\n");
    printf("P = (%.1f, %.1f, %.1f)\n", P[0], P[1], P[2]);
    printf("d = (%.1f, %.1f, %.1f)\n\n", d[0], d[1], d[2]);

    printf("Step 2: Plane in vector form\n");
    printf("n = (%.1f, %.1f, %.1f), n^T * r = %.1f\n\n", n[0], n[1], n[2], plane_constant);

    printf("Step 3: Solve for t\n");
    printf("t = (%.1f - %.1f)/%.1f = %.2f\n\n", plane_constant, numerator, denominator, t);

    printf("Step 4: Intersection point Q = P + t*d\n");
    printf("Q = (%.1f, %.1f, %.1f)\n\n", Q[0], Q[1], Q[2]);

    printf("Step 5: Vector PQ and its magnitude\n");
    printf("PQ = (%.1f, %.1f, %.1f)\n", PQ[0], PQ[1], PQ[2]);
    printf("|PQ| = sqrt(%.1f^2 + %.1f^2 + %.1f^2) = %.6f\n", PQ[0], PQ[1], PQ[2], PQ_length);

    printf("\nConclusion: The length of PQ = %.6f\n", PQ_length);

    // Write results into values.dat
    FILE *file = fopen("values.dat", "w");
    if(file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "Px\tPy\tPz\tDx\tDy\tDz\tNx\tNy\tNz\tPlaneConst\tT\tQx\tQy\tQz\tPQx\tPQy\tPQz\tPQLength\n");
    fprintf(file, "%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.2f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.1f\t%.6f\n",
            P[0], P[1], P[2], d[0], d[1], d[2], n[0], n[1], n[2], plane_constant, t,
            Q[0], Q[1], Q[2], PQ[0], PQ[1], PQ[2], PQ_length);

    fclose(file);
    printf("Results have been written to values.dat\n");

    return 0;
}

