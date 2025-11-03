#include <stdio.h>

int main() {
    // Given vertices
    int x1 , y1 ;   // A
    int x2 , y2 ;   // B
    int x3 , y3 ;   // C
    int x, y;             // D (to be calculated)

    // Using midpoint property: midpoint of AC = midpoint of BD
    x = x1 + x3 - x2;  // Derived formula
    y = y1 + y3 - y2;

    return 0;
}
