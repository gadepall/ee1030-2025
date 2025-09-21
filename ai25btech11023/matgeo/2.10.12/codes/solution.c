#include <stdio.h>
#include <math.h>

int main() {
    // Coordinates of the points
    double P[3] = {1, -1, 2};
    double Q[3] = {2, 0, -1};
    double R[3] = {0, 2, 1};

    // Store points to a file (no labels, just coordinates)
    FILE *fptr;
    fptr = fopen("output.data", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(fptr, "%lf %lf %lf\n", P[0], P[1], P[2]);
    fprintf(fptr, "%lf %lf %lf\n", Q[0], Q[1], Q[2]);
    fprintf(fptr, "%lf %lf %lf\n", R[0], R[1], R[2]);
    fclose(fptr);

    // Compute vectors PQ and PR
    double PQ[3], PR[3];
    for (int i = 0; i < 3; i++) {
        PQ[i] = Q[i] - P[i];
        PR[i] = R[i] - P[i];
    }

    // Cross product PQ x PR
    double N[3];
    N[0] = PQ[1]*PR[2] - PQ[2]*PR[1];
    N[1] = PQ[2]*PR[0] - PQ[0]*PR[2];
    N[2] = PQ[0]*PR[1] - PQ[1]*PR[0];

    // Magnitude of the vector N
    double mag = sqrt(N[0]*N[0] + N[1]*N[1] + N[2]*N[2]);

    // Unit vector
    double unit[3];
    for (int i = 0; i < 3; i++) {
        unit[i] = N[i];
    }

    printf("Unit vector perpendicular to the plane: (%lf, %lf, %lf)\n", unit[0], unit[1], unit[2]);
    return 0;
}
