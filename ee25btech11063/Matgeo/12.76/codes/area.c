#include <stdio.h>
#include <math.h>

int main() {
    // Coordinates
    float x[4] = {0, 0, -2, 2};
    float y[4] = {1, -3, -1, -1};
    float area;
    float sum1 = 0, sum2 = 0;

    // Shoelace formula: sum over vertices
    for(int i = 0; i < 4; i++) {
        int j = (i + 1) % 4;
        sum1 += x[i] * y[j];
        sum2 += y[i] * x[j];
    }
    area = fabs(sum1 - sum2) / 2.0;

    // Calculate side lengths
    float pq = sqrt(pow(x[1]-x[0],2) + pow(y[1]-y[0],2));
    float qr = sqrt(pow(x[2]-x[1],2) + pow(y[2]-y[1],2));
    float rs = sqrt(pow(x[3]-x[2],2) + pow(y[3]-y[2],2));
    float sp = sqrt(pow(x[0]-x[3],2) + pow(y[0]-y[3],2));

    // Check type
    char type[20];
    if (fabs(pq - qr) < 1e-3 && fabs(qr - rs) < 1e-3 && fabs(rs - sp) < 1e-3)
        sprintf(type, "Square");
    else if (fabs(pq - rs) < 1e-3 && fabs(qr - sp) < 1e-3)
        sprintf(type, "Rectangle");
    else
        sprintf(type, "Other Quadrilateral");

    // Write to file
    FILE *fp = fopen("area.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fp, "Area of the quadrilateral = %.2f\n", area);
    fprintf(fp, "Type of quadrilateral = %s\n", type);

    fclose(fp);

    printf("Output written to area.dat successfully.\n");
    return 0;
}

