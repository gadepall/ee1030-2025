#include <math.h>

// Analyze vector v with respect to u and w
void analyze_vector(double vx, double vy, double vz,
                    double ux, double uy, double uz,
                    double wx, double wy, double wz,
                    double *mag,     // magnitude of v
                    double *par_t,   // scalar t if parallel, else NAN
                    double *dot_vw)  // dot product v.w
{
    // magnitude
    *mag = sqrt(vx*vx + vy*vy + vz*vz);

    // dot product
    *dot_vw = vx*wx + vy*wy + vz*wz;
    // check parallel using cross product
    double cx = vy*uz - vz*uy;
    double cy = vz*ux - vx*uz;
    double cz = vx*uy - vy*ux;

    if (cx == 0 && cy == 0 && cz == 0) {
        // parallel → find scalar t
        if (ux != 0) *par_t = vx / ux;
        else if (uy != 0) *par_t = vy / uy;
        else if (uz != 0) *par_t = vz / uz;
        else *par_t = NAN; // u is zero vector
    } else {
        *par_t = NAN; // not parallel
    }
}