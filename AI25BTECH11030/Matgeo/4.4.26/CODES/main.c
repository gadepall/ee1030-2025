#include <stdio.h>
#include "trianglefun.h"

int main() {
    // Vertices of triangle
    int Ax = 2, Ay = 5;
    int Bx = -4, By = 9;
    int Cx = -2, Cy = -1;

    char equation[50];

    // Calculate the median equation and store as string
    median_equation(Ax, Ay, Bx, By, Cx, Cy, equation);

    // Print the equation
    printf("Equation of the median from A: %s\n", equation);

    return 0;
}
