#include <stdio.h>
#include <math.h>

// Function to compute area of triangle using cross product
float triangle_area(float Ax, float Ay, float Az,
                    float Bx, float By, float Bz,
                    float Cx, float Cy, float Cz) {
    // Vectors AB and AC
    float ABx = Bx - Ax;
    float ABy = By - Ay;
    float ABz = Bz - Az;

    float ACx = Cx - Ax;
    float ACy = Cy - Ay;
    float ACz = Cz - Az;

    // Cross product AB × AC
    float cross_x = ABy*ACz - ABz*ACy;
    float cross_y = ABz*ACx - ABx*ACz;
    float cross_z = ABx*ACy - ABy*ACx;

    // Area = 0.5 * |cross product|
    float area = 0.5 * sqrt(cross_x*cross_x + cross_y*cross_y + cross_z*cross_z);

    printf("Area of triangle ABC = %.2f\n", area);
    return area;
}
