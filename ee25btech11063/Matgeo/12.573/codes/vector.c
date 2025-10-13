#include <stdio.h>

int main() {
    // Given vectors
    float a[3] = {1, 2, 5};
    float b[3] = {1, 2, -1};

    // Variables for the unknown vector c = (x, y, z)
    // We will solve the system:
    // a·c = 0  =>  x + 2y + 5z = 0
    // b·c = 0  =>  x + 2y - z = 0

    float A[2][3] = {
        {1, 2, 5},
        {1, 2, -1}
    };
    float x, y, z;

    // Using elimination (matrix method):
    // Subtract equation 2 from equation 1
    // (1 - 1)x + (2 - 2)y + (5 - (-1))z = 0 - 0
    // => 6z = 0 => z = 0

    z = 0;

    // Substitute z = 0 in first equation:
    // x + 2y + 5*0 = 0 => x = -2y
    // Let y = 1 (for direction vector)

    y = 1;
    x = -2 * y;

    // Vector c is proportional to (-2, 1, 0)
    // Parallel vector can be written as (2, -1, 0)

    FILE *fp;
    fp = fopen("vector.dat", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "Vector c is parallel to: 2i - j\n");
    fprintf(fp, "Hence, c is parallel to (2, -1, 0)\n");

    fclose(fp);

    printf("Result written to vector.dat successfully.\n");

    return 0;
}

