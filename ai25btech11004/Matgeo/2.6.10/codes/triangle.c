#include <stdio.h>
#include <stdlib.h>

int main() {
    // Coordinates of vertices
    int x1 = -8, y1 = 4;
    int x2 = -6, y2 = 6;
    int x3 = -3, y3 = 9;

    // Apply determinant formula for area
    float area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2));

    // Open file to write output
    FILE *fp = fopen("triangle.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "The area of the triangle is: %.2f\n", area);

    fclose(fp);

    printf("Output written to triangle.dat successfully.\n");

    return 0;
}

