#include <math.h>
#include<stdio.h>
// Function to compute umbrella angle (in radians)
// vrw = velocity of rain relative to wind (2D vector)
// vw  = velocity of wind relative to ground (2D vector)
double umbrella_angle(double vrw[2], double vw[2]) {
    // Step 1: Resultant rain velocity relative to ground
    double vr[2];
    vr[0] = vw[0] + vrw[0];
    vr[1] = vw[1] + vrw[1];

    // Step 2: Downward unit vector
    double u_down[2] = {0.0, -1.0};

    // Step 3: Dot product
    double dot = vr[0]*u_down[0] + vr[1]*u_down[1];

    // Step 4: Norm of vr
    double norm_vr = sqrt(vr[0]*vr[0] + vr[1]*vr[1]);

    // Step 5: Angle from vertical (acos of normalized dot product)
    return acos(dot / norm_vr);   // radians
}
