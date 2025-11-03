#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y;
} Point;

// Function to compute distance between 2 points
double distance(Point a, Point b) {
    return sqrt((a.x - b.x)(a.x - b.x) + (a.y - b.y)(a.y - b.y));
}

int main() {
    double s = 3.4;                // side length
    double theta = 45.0;           // given angle in degrees
    double rad = theta * M_PI / 180.0; // convert to radians

    // Vertices
    Point A = {0, 0};
    Point B = {s, 0};
    Point D = {s * cos(rad), s * sin(rad)};
    Point C = {B.x + D.x - A.x, B.y + D.y - A.y};

    // Print vertices
    printf("Coordinates of rhombus:\n");
    printf("A(%.4f, %.4f)\n", A.x, A.y);
    printf("B(%.4f, %.4f)\n", B.x, B.y);
    printf("D(%.4f, %.4f)\n", D.x, D.y);
    printf("C(%.4f, %.4f)\n", C.x, C.y);

    // Verify equal sides
    printf("\nSide lengths:\n");
    printf("AB = %.4f\n", distance(A, B));
    printf("AD = %.4f\n", distance(A, D));
    printf("BC = %.4f\n", distance(B, C));
    printf("DC = %.4f\n", distance(D, C));

    return 0;
}
