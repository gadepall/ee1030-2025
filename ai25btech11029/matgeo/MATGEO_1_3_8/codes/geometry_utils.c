// geometry_utils.c
#include <stdio.h>

typedef struct {
    float x;
    float y;
} Point;

Point midpoint(Point a, Point b) {
    Point mid;
    mid.x = (a.x + b.x) / 2.0;
    mid.y = (a.y + b.y) / 2.0;
    return mid;
}

Point diagonal_midpoint(Point p1, Point p2) {
    return midpoint(p1, p2);
}

