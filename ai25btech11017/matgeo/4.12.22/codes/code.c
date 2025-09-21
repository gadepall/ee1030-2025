#include <stdio.h>

int main() {
    // Line: 3x - 4y - 8 = 0
    // Points
    int x1 = 3, y1 = 4;
    int x2 = 2, y2 = -6;

    // Evaluate f(x,y) = 3x - 4y - 8
    int f1 = 3*x1 - 4*y1 - 8;
    int f2 = 3*x2 - 4*y2 - 8;

    printf("Line equation: 3x - 4y - 8 = 0\n");

    printf("For point (3,4), f(x,y) = %d -> ", f1);
    if(f1 == 0) printf("Point lies on the line.\n");
    else if(f1 > 0) printf("Point lies on one side of the line.\n");
    else printf("Point lies on the other side of the line.\n");

    printf("For point (2,-6), f(x,y) = %d -> ", f2);
    if(f2 == 0) printf("Point lies on the line.\n");
    else if(f2 > 0) printf("Point lies on the same side as (3,4).\n");
    else printf("Point lies on the opposite side of (3,4).\n");

    // Final answer
    if ((f1 > 0 && f2 > 0) || (f1 < 0 && f2 < 0)) {
        printf("\nBoth points are on the SAME side of the line.\n");
    } else if (f1 == 0 || f2 == 0) {
        printf("\nOne of the points lies on the line.\n");
    } else {
        printf("\nThe points are on OPPOSITE sides of the line.\n");
    }

    return 0;
}
