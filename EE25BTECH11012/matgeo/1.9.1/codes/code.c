#include <stdio.h>
#include <math.h>

int main() {
    double m, n, distance;

    // Input values for m and n
    printf("Enter the value of m: ");
    scanf("%lf", &m);

    printf("Enter the value of n: ");
    scanf("%lf", &n);

    // Calculate distance using the formula
    distance = 2 * sqrt(m * m + n * n);

    // Print the result
    printf("Distance between the points (%.2lf, %.2lf) and (%.2lf, %.2lf) is: %.4lf\n",
           m, -n, -m, n, distance);

    return 0;
}
