#include <stdio.h>
#include <math.h>

int main() {
    double Ax, Ay, Az, Bx, By, Bz, K;
    double Mx, My, Mz, diffx, diffy, diffz;
    double diff_sq, r2, radius;

    // Input
    printf("Enter coordinates of A (x y z): ");
    scanf("%lf %lf %lf", &Ax, &Ay, &Az);

    printf("Enter coordinates of B (x y z): ");
    scanf("%lf %lf %lf", &Bx, &By, &Bz);

    printf("Enter constant K: ");
    scanf("%lf", &K);

    // Midpoint (center of sphere)
    Mx = (Ax + Bx) / 2.0;
    My = (Ay + By) / 2.0;
    Mz = (Az + Bz) / 2.0;

    // ||A-B||^2
    diffx = Ax - Bx;
    diffy = Ay - By;
    diffz = Az - Bz;
    diff_sq = diffx*diffx + diffy*diffy + diffz*diffz;

    // r^2 formula
    r2 = (2.0 * K * K - diff_sq) / 4.0;

    // Output
    printf("\n--- Results ---\n");
    printf("Point A = (%.2f, %.2f, %.2f)\n", Ax, Ay, Az);
    printf("Point B = (%.2f, %.2f, %.2f)\n", Bx, By, Bz);
    printf("K = %.2f\n", K);

    printf("Center M = (%.2f, %.2f, %.2f)\n", Mx, My, Mz);
    printf("r^2 = %.4f\n", r2);

    if (r2 < 0) {
        printf("No real sphere exists (r^2 < 0).\n");
    } else {
        radius = sqrt(r2);
        printf("Radius = %.4f\n", radius);

        printf("\nEquation of locus (vector form):\n");
        printf("|| P - (%.2f, %.2f, %.2f) ||^2 = %.4f\n", Mx, My, Mz, r2);
    }

    return 0;
}