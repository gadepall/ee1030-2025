/* triangle.c
   - writes points to "triangle.dat"
   - computes A' so that D'A' || DA and A' lies on extended BA
   - checks whether A' B C' D' is a parallelogram
*/
#include <stdio.h>
#include <math.h>

typedef struct { double x, y; } Point;

int areParallel(Point p1, Point p2, Point q1, Point q2) {
    double dx1 = p2.x - p1.x, dy1 = p2.y - p1.y;
    double dx2 = q2.x - q1.x, dy2 = q2.y - q1.y;
    return fabs(dy1 * dx2 - dy2 * dx1) < 1e-8;
}

int main(void) {
    FILE *fp = fopen("triangle.dat", "w");
    if (!fp) {
        perror("fopen");
        return 1;
    }

    /* Choose ABCD to be a parallelogram (so final shape will be a parallelogram).
       Example: rectangle/parallelogram with A=(0,0), B=(4,0), D=(0,3).
       Then C = B + D - A = (4,3).
    */
    Point A = {0.0, 0.0};
    Point B = {4.0, 0.0};
    Point D = {0.0, 3.0};
    Point C = { B.x + D.x - A.x, B.y + D.y - A.y }; /* ensures ABCD is parallelogram */

    double k = 4.0 / 3.0;

    /* BD'C' similar to BDC with scale factor k: D' = B + k*(D - B), C' = B + k*(C - B) */
    Point Dp = { B.x + k * (D.x - B.x), B.y + k * (D.y - B.y) };
    Point Cp = { B.x + k * (C.x - B.x), B.y + k * (C.y - B.y) };

    /* Solve for t where A' = B + t*(A - B) and D'A' || DA.
       Derivation:
         Let v = A - D.
         Let u(t) = (B - D') + t*(A - B).  (u = A' - D')
         Parallel condition: u.x * v.y - u.y * v.x = 0
       => t = [ (B.y - D'.y)*v.x - (B.x - D'.x)*v.y ]
              / [ (A.x - B.x)*v.y - (A.y - B.y)*v.x ]
    */
    double vx = A.x - D.x;
    double vy = A.y - D.y;
    double numerator  = (B.y - Dp.y) * vx - (B.x - Dp.x) * vy;
    double denominator = (A.x - B.x) * vy - (A.y - B.y) * vx;

    if (fabs(denominator) < 1e-12) {
        fprintf(stderr, "Denominator ~ 0: can't find unique A' (degenerate configuration)\n");
        fclose(fp);
        return 1;
    }

    double t = numerator / denominator;
    Point Ap = { B.x + t * (A.x - B.x), B.y + t * (A.y - B.y) };

    /* Write coordinates */
    fprintf(fp, "A  = (%.6f, %.6f)\n", A.x, A.y);
    fprintf(fp, "B  = (%.6f, %.6f)\n", B.x, B.y);
    fprintf(fp, "C  = (%.6f, %.6f)\n", C.x, C.y);
    fprintf(fp, "D  = (%.6f, %.6f)\n", D.x, D.y);
    fprintf(fp, "D' = (%.6f, %.6f)\n", Dp.x, Dp.y);
    fprintf(fp, "C' = (%.6f, %.6f)\n", Cp.x, Cp.y);
    fprintf(fp, "A' = (%.6f, %.6f)\n", Ap.x, Ap.y);

    /* Check parallelogram: opposite sides parallel */
    int cond1 = areParallel(Ap, B, Dp, Cp); /* A'B || D'C' */
    int cond2 = areParallel(Ap, Dp, B, Cp); /* A'D' || B C' */

    if (cond1 && cond2) {
        fprintf(fp, "\nA'BC'D' is a parallelogram.\n");
        printf("A'BC'D' is a parallelogram.\n");
    } else {
        fprintf(fp, "\nA'BC'D' is NOT a parallelogram.\n");
        printf("A'BC'D' is NOT a parallelogram.\n");
    }

    fclose(fp);
    return 0;
}

