#include <stdio.h>

int main() {
    // Given points (3,3), (6,y), (x,7), (5,6)
    // Using midpoint formula for diagonals:
    // Midpoint of diagonal 1: ((3 + x)/2, (3 + 7)/2)
    // Midpoint of diagonal 2: ((6 + 5)/2, (y + 6)/2)
    
    int x, y;
    
    // From midpoint x-coordinate equality
    x = 11 - 3;  // x = 8
    
    // From midpoint y-coordinate equality
    y = 10 - 6;  // y = 4
    
    printf("The values are:\nx = %d\ny = %d\n", x, y);
    
    return 0;
}
