#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Point through which the line passes
    double Px = -1.0, Py = 3.0, Pz = -2.0;

    // Direction ratios of given lines
    double d1x = 1.0, d1y = 2.0, d1z = 3.0;
    double d2x = -3.0, d2y = 2.0, d2z = 5.0;

    // Required direction vector d = (a, b, c)
    // Solved manually: d = (2, -7, 4)
    double dx = 2.0, dy = -7.0, dz = 4.0;

    // Vector equation of line: r = P + t*d

    // Distance from origin: 
    // t = -(P.d)/(d.d)
    double dotPd = Px*dx + Py*dy + Pz*dz;
    double dotDd = dx*dx + dy*dy + dz*dz;
    double t = -dotPd / dotDd;

    // Coordinates of foot of perpendicular Q = P + t*d
    double Qx = Px + t*dx;
    double Qy = Py + t*dy;
    double Qz = Pz + t*dz;

    // Distance = |OQ|
    double D = sqrt(Qx*Qx + Qy*Qy + Qz*Qz);

    // Print results to screen
    printf("Line passing through point P(-1, 3, -2)\n");
    printf("and perpendicular to the given two lines:\n");
    printf("(x-1)/1 = (y-1)/2 = (z+1)/3\n");
    printf("(x+2)/-3 = y/2 = z/5\n\n");

    printf("Direction vector of required line d = (%.0f, %.0f, %.0f)\n", dx, dy, dz);
    printf("Vector equation of line:\n");
    printf("r = (%.0f, %.0f, %.0f) + t(%.0f, %.0f, %.0f), t ∈ R\n\n",
           Px, Py, Pz, dx, dy, dz);

    printf("Foot of perpendicular from origin to line:\n");
    printf("Q = (%.4f, %.4f, %.4f)\n", Qx, Qy, Qz);
    printf("Distance from origin D = sqrt(5/69) ≈ %.4f\n\n", D);

    printf("Conclusion: The line is r = (%.0f, %.0f, %.0f) + t(%.0f, %.0f, %.0f)\n",
           Px, Py, Pz, dx, dy, dz);
    printf("and its distance from origin is %.4f\n", D);

    // Write results into a file
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "Px\tPy\tPz\tdx\tdy\tdz\tQx\tQy\tQz\tDistance\n");
    fprintf(file, "%.0f\t%.0f\t%.0f\t%.0f\t%.0f\t%.0f\t%.4f\t%.4f\t%.4f\t%.4f\n",
            Px, Py, Pz, dx, dy, dz, Qx, Qy, Qz, D);

    fclose(file);
    printf("Results have been written to values.dat\n");

    return 0;
}

