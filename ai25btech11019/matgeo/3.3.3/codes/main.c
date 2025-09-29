#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Side length of the equilateral triangle
    double side = 5.0;

    // Coordinates of A and B
    double Ax = 0.0, Ay = 0.0;
    double Bx = side, By = 0.0;

    // Angle at A = 60 degrees
    double angle_deg = 60.0;
    double angle_rad = angle_deg * M_PI / 180.0;

    // Coordinates of C
    double Cx = side * cos(angle_rad);
    double Cy = side * sin(angle_rad);

    // Print results to screen
    printf("Equilateral triangle with side = %.1f cm\n\n", side);
    printf("Vertex A = (%.1f, %.1f)\n", Ax, Ay);
    printf("Vertex B = (%.1f, %.1f)\n", Bx, By);
    printf("Vertex C = (%.2f, %.2f)\n\n", Cx, Cy);

    printf("Angle at A = %.1f degrees\n", angle_deg);
    printf("Coordinates of C calculated using:\n");
    printf("C = (side * cos(60°), side * sin(60°))\n");
    printf("C = (%.2f, %.2f)\n\n", Cx, Cy);

    printf("Conclusion: The equilateral triangle ABC has vertices:\n");
    printf("A(%.1f, %.1f), B(%.1f, %.1f), C(%.2f, %.2f)\n", 
           Ax, Ay, Bx, By, Cx, Cy);

    // Write results into a file
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "Ax\tAy\tBx\tBy\tCx\tCy\tAngleA\n");
    fprintf(file, "%.1f\t%.1f\t%.1f\t%.1f\t%.2f\t%.2f\t%.1f\n",
            Ax, Ay, Bx, By, Cx, Cy, angle_deg);

    fclose(file);
    printf("Results have been written to values.dat\n");

    return 0;
}

