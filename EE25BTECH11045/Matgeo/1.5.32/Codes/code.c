#include <stdio.h>
// Structure for a 2D point/vector

typedef struct {
    double x;
    double y;
} Point;

// Function to apply section formula

Point sectionFormula(Point A, Point B, double m, double n) {
   Point P;
     P.x = (m * B.x + n * A.x) / (m + n);
     P.y = (m * B.y + n * A.y) / (m + n);
    return P;
}