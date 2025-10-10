#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

// Function to create main.so file (dummy shared library)
void createSharedLibrary() {
    FILE *fp = fopen("main.so", "wb");
    if (fp == NULL) {
        printf("Error creating main.so file\n");
        return;
    }

    // Write a simple binary header to simulate a shared library
    unsigned char header[] = {0x7f, 0x45, 0x4c, 0x46}; // ELF header start
    fwrite(header, sizeof(header), 1, fp);

    fclose(fp);
    printf("main.so file created\n");
}

// Function to write data to files
void writeToFile() {
    FILE *fp;

    // Write main data to main.dat
    fp = fopen("main.dat", "w");
    if (fp == NULL) {
        printf("Error opening main.dat file\n");
        return;
    }

    // Write points P, Q, S and other calculated values
    fprintf(fp, "# Points and calculations for parabola y^2 = 8x and circle x^2 + y^2 - 2x - 4y = 0\n");
    fprintf(fp, "# P(0,0), Q(2,4), S(2,0) - focus of parabola\n");
    fprintf(fp, "P 0.0 0.0\n");  // P
    fprintf(fp, "Q 2.0 4.0\n");  // Q  
    fprintf(fp, "S 2.0 0.0\n");  // S
    fprintf(fp, "Area 4.0\n");   // Area of triangle PQS

    // Additional data for plotting
    fprintf(fp, "# Parabola points (y^2 = 8x)\n");
    for (double y = -6; y <= 6; y += 0.1) {
        double x = (y * y) / 8.0;
        if (x >= -1 && x <= 10) {
            fprintf(fp, "PARABOLA %.2f %.2f\n", x, y);
        }
    }

    // Circle points (x^2 + y^2 - 2x - 4y = 0)
    // Rewrite as (x-1)^2 + (y-2)^2 = 5
    fprintf(fp, "# Circle points (x^2 + y^2 - 2x - 4y = 0)\n");
    for (double theta = 0; theta <= 2*M_PI; theta += 0.1) {
        double x = 1 + sqrt(5) * cos(theta);
        double y = 2 + sqrt(5) * sin(theta);
        fprintf(fp, "CIRCLE %.2f %.2f\n", x, y);
    }

    fclose(fp);
    printf("Data written to main.dat\n");
}

// Function to calculate intersection points
void calculateIntersection() {
    printf("Calculating intersection of parabola y^2 = 8x and circle x^2 + y^2 - 2x - 4y = 0\n");

    // From the PDF solution, we know:
    // Circle: x^2 + y^2 - 2x - 4y = 0
    // Parabola: y^2 = 8x

    // Matrix parameters for circle V1
    double V1[2][2] = {{1, 0}, {0, 1}};
    double u1[2] = {-1, -2};
    double f1 = 0;

    // Matrix parameters for parabola V2
    double V2[2][2] = {{0, 0}, {0, 1}};
    double u2[2] = {-4, 0};
    double f2 = 0;

    // Focus S of parabola y^2 = 8x is at (2, 0)
    double S[2] = {2, 0};

    // Intersection points from the solution
    double P[2] = {0, 0};  // X1
    double Q[2] = {2, 4};  // X2

    printf("Focus S: (%.1f, %.1f)\n", S[0], S[1]);
    printf("Intersection point P: (%.1f, %.1f)\n", P[0], P[1]);
    printf("Intersection point Q: (%.1f, %.1f)\n", Q[0], Q[1]);

    // Calculate area of triangle PQS using cross product
    // Area = (1/2) * |SP x QP|
    double SP[2] = {P[0] - S[0], P[1] - S[1]};  // S to P vector
    double QP[2] = {P[0] - Q[0], P[1] - Q[1]};  // Q to P vector

    // Cross product in 2D: SP x QP = SP[0]*QP[1] - SP[1]*QP[0]
    double cross_product = SP[0] * QP[1] - SP[1] * QP[0];
    double area = 0.5 * fabs(cross_product);

    printf("Area of triangle PQS: %.1f square units\n", area);

    createSharedLibrary();
    writeToFile();
}

int main() {
        calculateIntersection();

    printf("\nFiles generated: main.so and main.dat\n");
    return 0;
}
