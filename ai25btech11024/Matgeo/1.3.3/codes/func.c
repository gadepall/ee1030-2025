#include <stdio.h>

// Struct to represent a 2D point
typedef struct {
    int x;
    int y;
} Point;

// Function to compute C = D + B - A
Point find_point_c(Point A, Point B, Point D) {
    Point C;
    C.x = D.x + B.x - A.x;
    C.y = D.y + B.y - A.y;
    return C;
}