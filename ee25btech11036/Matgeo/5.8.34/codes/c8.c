// triangle.c
#include <stdio.h>

typedef struct {
    double x;
    double y;
} Point;

void get_triangle_vertices(Point* A, Point* B, Point* C) {
    A->x = -1; A->y = 0;
    B->x = 4;  B->y = 0;
    C->x = 2;  C->y = 3;
}

