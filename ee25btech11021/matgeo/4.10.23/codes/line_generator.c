/* line_generator.c */
#include <stdio.h>

/* Generate points along line N^T x + c = 0
   Nx, Ny = components of normal vector
   c = constant
   tmin, tmax = steps along direction perpendicular to N
*/
void generate_line_points(double Nx, double Ny, double c, int tmin, int tmax) {
    double dx = -Ny;  // direction vector perpendicular to normal
    double dy = Nx;

    // Pick a point on the line: x0 = 0, y0 = -c/Ny
    double x0 = 0.0;
    double y0 = -c / Ny;

    for (int t = tmin; t <= tmax; t++) {
        double x = x0 + t*dx;
        double y = y0 + t*dy;
        printf("%.6f %.6f\n", x, y);
    }
}


