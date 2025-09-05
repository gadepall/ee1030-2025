#include <stdio.h>

int main() {
// Given points A and B
double Ax = 1, Ay = 2;
double Bx = 2, By = 3;

// Given x-coordinate of P
double Px = 8;
double Py;

// Solve for Py using rank condition:
// For matrix [[1, Px - Ax], [1, Py - Ay]] to have rank 1,
// second column must be proportional:
// => (Px - Ax) - (Py - Ay) = 0 => Py = Px - Ax + Ay
Py = Px - Ax + Ay;
printf("Calculated y-coordinate of P: %lf\n", Py);

// Calculate ratio k using section formula rearrangement
double numerator = (Ax - Px)*(Px - Bx) + (Ay - Py)*(Py - By);
double denominator = (Px - Bx)*(Px - Bx) + (Py - By)*(Py - By);

double k = numerator / denominator;

printf("Ratio k in which P divides AB: %lf\n", k);

return 0;
}