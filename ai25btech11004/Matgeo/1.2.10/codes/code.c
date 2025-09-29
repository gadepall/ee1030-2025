#include <stdio.h>

int main() {
    FILE *fp;

    // Coordinates of P and Q
    int Px = 2, Py = 3, Pz = 0;
    int Qx = -1, Qy = -2, Qz = -4;

    // Vector from P to Q: Q - P
    int Vx = Qx - Px;
    int Vy = Qy - Py;
    int Vz = Qz - Pz;

    // Open file for writing
    fp = fopen("vector.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write vector to file
    fprintf(fp, "Vector from P(%d,%d,%d) to Q(%d,%d,%d):\n", Px, Py, Pz, Qx, Qy, Qz);
    fprintf(fp, "Vector PQ = (%d, %d, %d)\n", Vx, Vy, Vz);

    // Close file
    fclose(fp);

    printf("Vector successfully written to vector.dat\n");
    return 0;
}

