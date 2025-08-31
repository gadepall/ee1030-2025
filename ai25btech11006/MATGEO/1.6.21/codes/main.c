#include <stdio.h>
#include "func.h"

int main() {
    double a, b, c;
    printf("Enter a, b, c: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    // Points
    double A[2] = {a, b+c};
    double B[2] = {b, c+a};
    double C[2] = {c, a+b};

    // Save points to file for plotting
    FILE *fp = fopen("points.dat", "w");
    if (fp != NULL) {
        fprintf(fp, "%lf %lf\n", A[0], A[1]);
        fprintf(fp, "%lf %lf\n", B[0], B[1]);
        fprintf(fp, "%lf %lf\n", C[0], C[1]);
        fclose(fp);
    }

    // Check collinearity
    int result = check_collinear(a, b, c);
    if (result)
        printf("The points are collinear.\n");
    else
        printf("The points are not collinear.\n");

    return 0;
}

