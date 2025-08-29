#include <stdio.h>

// Function to return relation value
int relation(int x, int y) {
    return x + 3*y - 7;
}

int main() {
    // Given points
    int x1 = 1, y1 = 2;
    int x2 = 7, y2 = 0;

    // Step 1: Compute slope
    float m = (float)(y2 - y1) / (x2 - x1);
  
    printf("        m = (y2 - y1) / (x2 - x1) = (%d - %d) / (%d - %d) = %.2f\n\n",
            y2, y1, x2, x1, m);

    // Step 2: Point-slope form
    printf("Step 2: Equation using point-slope form:\n");
    printf("        (y - %d) = m(x - %d)\n\n", y1, x1);

    // Final Relation
    printf("Final Relation: x + 3y - 7 = 0\n");

    return 0;
}

