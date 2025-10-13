#include <stdio.h>

int main() {
    FILE *fp;
    float a = 1, b = 2, c = 3, d = 4;
    float det, inv[2][2];

    det = a * d - b * c;

    if(det == 0) {
        printf("Inverse does not exist (determinant is zero).\n");
        return 0;
    }

    // Compute inverse
    inv[0][0] =  d / det;
    inv[0][1] = -b / det;
    inv[1][0] = -c / det;
    inv[1][1] =  a / det;

    // Open file to write
    fp = fopen("inverse.dat", "w");
    if(fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "The inverse of the matrix is:\n");
    fprintf(fp, "[ %.2f  %.2f ]\n", inv[0][0], inv[0][1]);
    fprintf(fp, "[ %.2f  %.2f ]\n", inv[1][0], inv[1][1]);

    fclose(fp);

    printf("Inverse matrix has been written to inverse.dat successfully.\n");

    return 0;
}

