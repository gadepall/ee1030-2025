#include <stdio.h>
#include <math.h>

int main() {
    // Given points
    double A[2] = {2.0, 6.0};
    double B[2] = {5.0, -4.0};
    // C = (k,4) but k unknown

    // Compute B - A
    double BA[2] = {B[0] - A[0], B[1] - A[1]}; // (3,-10)

    // We know area = 35
    double area = 35.0;

    // |10k - 26| = 70
    // Solve for k:
    double k1 = (70.0 + 26.0)/10.0;   // (10k-26)=70
    double k2 = (-70.0 + 26.0)/10.0;  // (10k-26)=-70

    // Print to screen
    printf("B - A = (%.1f, %.1f)\n", BA[0], BA[1]);
    printf("Area = %.1f\n", area);
    printf("Possible k values:\n");
    printf("k1 = %.6f\n", k1);
    printf("k2 = %.6f\n", k2);

    // Write to dat file
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "BminusA_x\tBminusA_y\tArea\tk1\tk2\n");
    fprintf(file, "%.1f\t%.1f\t%.1f\t%.6f\t%.6f\n",
            BA[0], BA[1], area, k1, k2);

    fclose(file);
    printf("Results have been written to values.dat\n");

    return 0;
}

