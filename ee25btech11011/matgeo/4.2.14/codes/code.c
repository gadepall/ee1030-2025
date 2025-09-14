#include <stdio.h>

/* Dot product of 2D vectors */
int dot_product(int a[2], int b[2]) {
    return a[0]*b[0] + a[1]*b[1];
}

/* Check if two vectors are orthogonal */
int is_orthogonal(int a[2], int b[2]) {
    return dot_product(a, b) == 0;
}

/* Equation of the line: x + y = 0  -> y = -x */
double line_equation(double x) {
    return -x;
}

/* Example test */
int main(void) {
    int n[2] = {1, 1};    // normal vector
    int m[2] = {-1, 1};   // direction vector

    printf("Dot product of n and m = %d\n", dot_product(n, m));
    printf("Are n and m orthogonal? %s\n", is_orthogonal(n, m) ? "Yes" : "No");

    for (double X = -5; X <= 5; X += 2.5) {
        printf("For x = %.2f, y = %.2f (on line x+y=0)\n", X, line_equation(X));
    }

    return 0;
}
