#include <stdio.h>

typedef struct {
    double x;
    double y;
} Vector2D;

// Function to compute direction and normal vectors
void computeVectors(Vector2D p1, Vector2D p2, Vector2D *direction, Vector2D *normal) {
    direction->x = p2.x - p1.x;
    direction->y = p2.y - p1.y;

    normal->x = -(direction->y);
    normal->y = direction->x;
}
