#ifndef TRIANGLEFUN_H
#define TRIANGLEFUN_H

typedef struct {
    double x;
    double y;
} Point;

// Function to construct the right triangle points
void construct_right_triangle(Point* A, Point* B, Point* C);

#endif // TRIANGLEFUN_H
