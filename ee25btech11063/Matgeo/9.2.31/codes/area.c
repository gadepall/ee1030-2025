#include <stdio.h>
#include <math.h>

// Corrected function: f(y) = 2*sqrt(y) - y^2/4
double f(double y) {
    return 2 * sqrt(y) - (pow(y, 2) / 4.0);
}

int main() {
    double a = 0.0, b = 4.0; // Limits of integration
    int n = 100000; // Number of intervals
    double h = (b - a) / n;
    double area = 0.0;

    for (int i = 1; i < n; i++) {
        double y = a + i * h;
        area += f(y);
    }

    area += (f(a) + f(b)) / 2.0;
    area *= h;

    // Write the result to area.dat
    FILE *fp = fopen("area.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(fp, "The area bounded by the curves is: %.6lf\n", area);
    fclose(fp);

    return 0;
}

