
#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp = fopen("ellipse.dat", "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    double a = 3.0;          // semi-major axis (x-direction)
    double b = sqrt(5.0);    // semi-minor axis (y-direction)
    double theta;

    for (theta = 0; theta <= 2*M_PI; theta += 0.01) {
        double x = a * cos(theta);
        double y = b * sin(theta);
        fprintf(fp, "%lf %lf\n", x, y);
    }

    fclose(fp);
    printf("Data written to ellipse.dat\n");
    printf("Use: gnuplot -e \"plot 'ellipse.dat' with lines title 'x^2/9 + y^2/5 = 1'\"\n");
    return 0;
}
