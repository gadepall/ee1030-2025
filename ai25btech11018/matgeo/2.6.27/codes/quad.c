#include <stdio.h>
#include <stdlib.h>

struct Point {
    int x, y;
};

// Function to calculate the cross product (magnitude) of vectors u and v
int crossProduct(int ux, int uy, int vx, int vy) {
    return ux * vy - uy * vx;
}

// Function to calculate area of triangle given vertices p1, p2, p3 using vectors
double triangleArea(struct Point p1, struct Point p2, struct Point p3) {
	int ux = p2.x - p1.x;
    int uy = p2.y - p1.y;
    int vx = p3.x - p1.x;
    int vy = p3.y - p1.y;

    int cross = crossProduct(ux, uy, vx, vy);
    return abs(cross) / 2.0;
}

int main() {
    struct Point A = {-5, 7};
    struct Point B = {-4, -5};
    struct Point C = {-1, -6};
    struct Point D = {4, 5};
// Calculate areas of triangles ABC and ACD
    double areaABC = triangleArea(A, B, C);
    double areaACD = triangleArea(A, C, D);

    // Total area of quadrilateral ABCD
    double areaABCD = areaABC + areaACD;

    printf("Area of quadrilateral ABCD = %.2f\n", areaABCD);

    return 0;
}
    
