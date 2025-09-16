#include <stdio.h>

// Function to compute required plane coefficients
// Input: n1,d1,n2,d2,n3,d3
// Output: n_req[], d_req
void required_plane(double n1[3], double d1,
                    double n2[3], double d2,
                    double n3[3], double d3,
                    double n_req[3], double *d_req) {
    
    // Find λ such that (n1 + λn2)·n3 = 0
    double dot_n1n3 = n1[0]*n3[0] + n1[1]*n3[1] + n1[2]*n3[2];
    double dot_n2n3 = n2[0]*n3[0] + n2[1]*n3[1] + n2[2]*n3[2];
    double lam = -dot_n1n3 / dot_n2n3;

    // Required normal = n1 + λ n2
    for(int i=0; i<3; i++) {
        n_req[i] = n1[i] + lam * n2[i];
    }

    // Required constant term
    *d_req = d1 + lam * d2;
}

