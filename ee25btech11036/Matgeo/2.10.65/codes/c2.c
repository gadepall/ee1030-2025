// parallelogram.c
#include <stdio.h>

typedef struct {
    double x;
    double y;
} Point;

// Use static storage to return struct (safer when returning to external code)
static Point result;

Point intersection() {
    Point O = {0.0, 0.0};
    Point A = {1.0, 0.0};
    Point B = {0.0, 1.0};
    Point D = {(O.x + A.x)/2.0, (O.y + A.y)/2.0};

    double lam = 2.0/3.0;
    result.x = B.x + lam * (D.x - B.x);
    result.y = B.y + lam * (D.y - B.y);

    return result;
}

