#include <stdio.h>

// Function to find ratio k:1 in which line divides the segment
float findRatio(int a, int b, int c, int x1, int y1, int x2, int y2) {
    // Equation: a(k*x2 + x1) + b(k*y2 + y1) + c(k+1) = 0
    int A = a*x2 + b*y2 + c;   // coefficient of k
    int B = a*x1 + b*y1 + c;   // constant term

    float k = (float)(-B) / A; // ratio k:1
    return k;
}

// Function to find coordinates of point of division
void findDivisionPoint(float k, int x1, int y1, int x2, int y2) {
    float x = (k*x2 + x1) / (k+1);
    float y = (k*y2 + y1) / (k+1);

    printf("Point of division: (%.2f, %.2f)\n", x, y);
}