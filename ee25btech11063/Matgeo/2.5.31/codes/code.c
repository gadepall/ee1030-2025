#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("triangle.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Given vertices
    double x1 = 3, y1 = 0;
    double x2 = 6, y2 = 0;

    // Midpoint of AB
    double xm = (x1 + x2) / 2.0;
    double ym = (y1 + y2) / 2.0;

    // Length of AB
    double side = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1));

    // Height of equilateral triangle
    double h = (sqrt(3) / 2.0) * side;

    // Two possible third vertices
    double x3a = xm;
    double y3a = ym + h;

    double x3b = xm;
    double y3b = ym - h;

    // Writing results to file
    fprintf(fp, "First vertex: (%.2f, %.2f)\n", x1, y1);
    fprintf(fp, "Second vertex: (%.2f, %.2f)\n", x2, y2);
    fprintf(fp, "Third vertex (above x-axis): (%.2f, %.2f)\n", x3a, y3a);
    fprintf(fp, "Third vertex (below x-axis): (%.2f, %.2f)\n", x3b, y3b);

    fclose(fp);

    printf("Results written to triangle.dat successfully.\n");
    return 0;
}

