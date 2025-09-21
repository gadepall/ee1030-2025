#include <stdio.h>
#include <math.h>

// Function to compute angle between two 3D vectors
double angle_between(double *u, double *v) {
    // dot product
    double dot = u[0]*v[0] + u[1]*v[1] + u[2]*v[2];
    // norms
    double norm_u = sqrt(u[0]*u[0] + u[1]*u[1] + u[2]*u[2]);
    double norm_v = sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
    // cosine formula
    double cos_theta = dot / (norm_u * norm_v);
    // clip for numerical safety
    if(cos_theta > 1.0) cos_theta = 1.0;
    if(cos_theta < -1.0) cos_theta = -1.0;
    // angle in radians
    return acos(cos_theta);
}

/* Build as shared library:
   gcc -fPIC -shared -o func.so func.c -lm
*/

