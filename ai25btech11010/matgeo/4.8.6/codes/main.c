#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "/home/dhanush-kumar-a/ee1030-2025/ai25btech11010/matgeo/4.8.6/codes/libs/matfun.h"

// Function to compute distance and reflection
// Inputs: P (3x1), n (3x1), d
// Outputs: distance (pointer), R (3x1 array)
void point_plane_info(double **P, double **n, double d, double *distance, double *R) {
    // Compute lambda
    double lam = (Matdot(n,P,3) - d)/(Matdot(n,n,3));

    // Compute foot of perpendicular Q = P - lambda*n
    double **Q = Matsub(P, Matscale(n,3,1,lam), 3,1);

    // Compute distance = |lambda| * ||n||
    *distance = fabs(lam) * Matnorm(n,3);

    // Compute reflection R = 2*Q - P
    double **Rmat = Matsub(Matscale(Q,3,1,2.0), P, 3,1);

    // Copy results to output array
    for(int i=0;i<3;i++)
        R[i] = Rmat[i][0];

    // Free memory
    for(int i=0;i<3;i++){
        free(Q[i]);
        free(Rmat[i]);
    }
    free(Q);
    free(Rmat);
}

