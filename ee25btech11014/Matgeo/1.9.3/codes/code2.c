#include <stdio.h>
#include <math.h>

int main() {
    // Coordinates of points
    int x1 = 0, y1 = -3;  // A
    int x2 = 4, y2 = 0;   // B

    // Calculate diagonal length using distance formula
    double diagonal = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    printf("The length of the diagonal of rectangle AOBC is: %.2f\n", diagonal);

    return 0;
}
