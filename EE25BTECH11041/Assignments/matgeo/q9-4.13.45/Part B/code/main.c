// main.c
// Compile with: gcc -shared -o libbisector.so -fPIC main.c -lm

#include <stdio.h>
#include <math.h>

typedef struct {
    double a;
    double b;
    double c;
} Line;

// helper: clamp for acos
static double clamp(double v, double lo, double hi){
    if(v < lo) return lo;
    if(v > hi) return hi;
    return v;
}

// compute direction vector (dx,dy) for line ax+by+c=0
// direction vector = (b, -a)
static void dir_vector(double a, double b, double *dx, double *dy){
    *dx = b;
    *dy = -a;
}

// angle between directions (dx1,dy1) and (dx2,dy2) in [0, pi]
static double angle_between(double dx1, double dy1, double dx2, double dy2){
    double dot = dx1*dx2 + dy1*dy2;
    double n1 = sqrt(dx1*dx1 + dy1*dy1);
    double n2 = sqrt(dx2*dx2 + dy2*dy2);
    if(n1==0 || n2==0) return 0.0;
    double cosv = clamp(dot/(n1*n2), -1.0, 1.0);
    return acos(cosv);
}

// Solve intersection of two lines. returns 1 if solvable, 0 if parallel.
static int intersect_point(double a1,double b1,double c1,double a2,double b2,double c2, double *x, double *y){
    double D = a1*b2 - a2*b1;
    if(fabs(D) < 1e-12) return 0;
    *x = (b1*c2 - b2*c1) / D;
    *y = (a2*c1 - a1*c2) / D;
    return 1;
}

// API: compute the obtuse-angle bisector line coefficients into result
Line obtuse_bisector(double a1, double b1, double c1, double a2, double b2, double c2){
    Line res = {0,0,0};

    // normalization factors
    double s1 = sqrt(a1*a1 + b1*b1);
    double s2 = sqrt(a2*a2 + b2*b2);
    if(s1 == 0 || s2 == 0){
        return res;
    }

    // Build the two candidate bisector lines:
    // (+) => (a1/s1 - a2/s2) x + (b1/s1 - b2/s2) y + (c1/s1 - c2/s2) = 0
    // (-) => (a1/s1 + a2/s2) x + (b1/s1 + b2/s2) y + (c1/s1 + c2/s2) = 0
    Line Lplus, Lminus;
    Lplus.a =  a1/s1 - a2/s2;
    Lplus.b =  b1/s1 - b2/s2;
    Lplus.c =  c1/s1 - c2/s2;

    Lminus.a =  a1/s1 + a2/s2;
    Lminus.b =  b1/s1 + b2/s2;
    Lminus.c =  c1/s1 + c2/s2;

    // We need to choose which of Lplus or Lminus is the bisector of the obtuse angle.
    // Strategy:
    //  - compute direction vectors of original lines and the two bisectors
    //  - compute the small angle between L1 and L2 (in [0, pi/2])
    //  - for each bisector compute its angle with L1 (in [0, pi])
    //  - the bisector corresponding to the obtuse angle will make an angle > pi/4 with L1
    // This numeric test is stable for non-degenerate cases.

    double dx1, dy1;
    dir_vector(a1, b1, &dx1, &dy1);
    double dx2, dy2;
    dir_vector(a2, b2, &dx2, &dy2);

    double theta = angle_between(dx1, dy1, dx2, dy2);
    if(theta > M_PI_2) theta = M_PI - theta; // small angle in [0, pi/2]

    // bisector directions
    double dpx, dpy, dmx, dmy;
    dir_vector(Lplus.a, Lplus.b, &dpx, &dpy);
    dir_vector(Lminus.a, Lminus.b, &dmx, &dmy);

    double alpha_plus  = angle_between(dx1, dy1, dpx, dpy);
    double alpha_minus = angle_between(dx1, dy1, dmx, dmy);

    // The bisector of the obtuse angle will have alpha > pi/4 (because obtuse half-angle > pi/4).
    if(alpha_plus > alpha_minus){
        // Choose plus if it gives larger angle
        res = Lplus;
    } else {
        res = Lminus;
    }

    // Optionally normalize so that sqrt(a^2+b^2)=1 and keep sign consistent
    double norm = sqrt(res.a*res.a + res.b*res.b);
    if(norm > 1e-12){
        res.a /= norm;
        res.b /= norm;
        res.c /= norm;
    }

    // ensure consistent sign: make a >= 0 or if a==0 ensure b>=0
    if(res.a < -1e-12 || (fabs(res.a) < 1e-12 && res.b < -1e-12)){
        res.a = -res.a; res.b = -res.b; res.c = -res.c;
    }

    return res;
}

// If used from command line for quick test
#ifdef TEST_C
int main(){
    // Given example: x - 2y + 4 = 0  and 4x - 3y + 2 = 0
    double a1=1, b1=-2, c1=4;
    double a2=4, b2=-3, c2=2;
    Line obt = obtuse_bisector(a1,b1,c1,a2,b2,c2);
    printf("Obtuse bisector: %.6f x + %.6f y + %.6f = 0\n", obt.a, obt.b, obt.c);
    return 0;
}
#endif

