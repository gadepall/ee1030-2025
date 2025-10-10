#include <stdio.h>

int main() {
    double Ax, Ay, Bx, By, dx, dy, slope;

    // Input coordinates of points A and B
    printf("Enter coordinates of point A (x y): ");
    scanf("%lf %lf", &Ax, &Ay);

    printf("Enter coordinates of point B (x y): ");
    scanf("%lf %lf", &Bx, &By);

    // Direction vector components (B - A)
    dx = Bx - Ax; // horizontal component
    dy = By - Ay; // vertical component

    // Check for vertical line (undefined slope)
    if (dx == 0) {
        printf("The line AB is vertical. The slope is undefined (infinite).\n");
    } else {
        slope = dy / dx;
        printf("Direction vector of AB: (%.2f, %.2f)\n", dx, dy);
        printf("Slope of AB: %.2f\n", slope);
    }

    return 0;
}
