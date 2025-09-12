#include <stdio.h>
#include <math.h>

int main() {
    // Coordinates of the point
    int x = -6;
    int y = 8;

    // Calculate the distance using the Euclidean formula
    double distance = sqrt(x * x + y * y);

    // Display the result
    printf("The distance of the point P = (%d, %d) from the origin is %.2f units.\n", x, y, distance);

    return 0;
}
