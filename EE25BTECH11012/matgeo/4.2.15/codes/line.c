#include <stdio.h>

// A simple structure to represent a 2D vector
typedef struct {
    float x;
    float y;
} Vector2D;

int main() {
    // Equation of the line: y = 2x
    // General form: 2x - 1y + 0 = 0
    // So, A = 2 and B = -1

    float A = 2.0f;
    float B = -1.0f;

    // Declare vectors
    Vector2D normal_vector;
    Vector2D direction_vector;

    // --- Calculation ---

    // For a line Ax + By + C = 0:
    // A normal vector is given by n = (A, B)
    normal_vector.x = A;
    normal_vector.y = B;

    // A direction vector is perpendicular to the normal vector.
    // It can be found as d = (-B, A) or (B, -A)
    direction_vector.x = -B;
    direction_vector.y = A;

    // --- Output ---

    printf("For the line y = 2x (or 2x - y = 0):\n");
    printf("----------------------------------------\n");
    printf("Calculated Normal Vector   (A, B)  : <%.1f, %.1f>\n", normal_vector.x, normal_vector.y);
    printf("Calculated Direction Vector (-B, A): <%.1f, %.1f>\n", direction_vector.x, direction_vector.y);

    return 0;
}