#include <stdio.h>
#include <math.h>

// Solve the midpoint + constraint problem
// A = (Ax, Ay)
// B = (k, By)   (Bx is unknown, denoted k)
// Constraint:   p*a + q*b = r,  where (a,b) is midpoint
//
// Outputs:
//   *a, *b  → midpoint coordinates
//   *k      → solved x-coordinate of B
//   *ABx,*ABy → vector A-B
//   *norm2  → squared distance (A-B).(A-B)
void solve_problem(double Ax, double Ay, double By,
                   double p, double q, double r,
                   double *a, double *b, double *k,
                   double *ABx, double *ABy, double *norm2)
{
    // Midpoint coordinates
    *b = (Ay + By) / 2.0;
    *k = (2.0 * r - p * Ax - 2.0 * q * (*b)) / p;
    *a = (Ax + *k) / 2.0;

    // Vector A - B
    *ABx = Ax - *k;
    *ABy = Ay - By;

    // Squared distance
    *norm2 = (*ABx) * (*ABx) + (*ABy) * (*ABy);
}
