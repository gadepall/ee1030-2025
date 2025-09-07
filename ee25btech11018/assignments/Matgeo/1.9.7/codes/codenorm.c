#include <stdio.h>
#include <math.h>

// Function to compute distance from origin
double norm(int x, int y) {
    return sqrt(x*x + y*y);
}

int main() {
    int x = -6, y = 8;
    printf("Given point: (%d, %d)\n", x, y);
    double distance = norm(x,y);
    printf("Therefore, the distance of the point (%d, %d) from the origin is %.2f units.\n", x, y, distance);
    return 0;
}

