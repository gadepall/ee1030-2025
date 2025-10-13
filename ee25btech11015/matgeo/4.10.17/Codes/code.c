#include <math.h>

// Function to compute area of a triangle given 3 points (x,y,z)
float triangle_area(float x1, float y1, float z1,
                    float x2, float y2, float z2,
                    float x3, float y3, float z3) {

    // Using cross product method: Area = 0.5 * |AB x AC|
    float ABx = x2 - x1;
    float ABy = y2 - y1;
    float ABz = z2 - z1;

    float ACx = x3 - x1;
    float ACy = y3 - y1;
    float ACz = z3 - z1;

    // Cross product AB x AC
    float cross_x = ABy*ACz - ABz*ACy;
    float cross_y = ABz*ACx - ABx*ACz;
    float cross_z = ABx*ACy - ABy*ACx;

    // Magnitude of cross product
    float area = 0.5 * sqrt(cross_x*cross_x + cross_y*cross_y + cross_z*cross_z);
    return area;
}
