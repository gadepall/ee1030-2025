// file: unitvec3d.c
#include <math.h>

// Compute unit vector from P to Q in 3D
// Inputs: P[3], Q[3]
// Output: unit[3]
// Returns: 0 on success, -1 if P=Q
 int unit_vector_3d(const double* P, const double* Q, double* unit) {
    double dx = Q[0] - P[0];
    double dy = Q[1] - P[1];
    double dz = Q[2] - P[2];
    double norm = sqrt(dx*dx + dy*dy + dz*dz);
    if (norm == 0.0) return -1;
    unit[0] = dx / norm;
    unit[1] = dy / norm;
    unit[2] = dz / norm;
    return 0;
}


