#include <stdio.h>

int main() {
    // Input: position vectors of A and B
    float ax, ay, bx, by;
    
    printf("Enter coordinates of A (ax ay): ");
    scanf("%f %f", &ax, &ay);

    printf("Enter coordinates of B (bx by): ");
    scanf("%f %f", &bx, &by);

    // External division ratio k:1, here k = 3
    int k = 3;

    // Using section formula for external division:
    // C = (k*b - a) / (k - 1)
    float cx = (k*bx - ax) / (k - 1);
    float cy = (k*by - ay) / (k - 1);

    printf("Position vector of C is: (%.2f, %.2f)\n", cx, cy);

    return 0;
}