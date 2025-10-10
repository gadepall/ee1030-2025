#include <stdio.h>
#include <math.h>
#include "libs/matfun.h"

void get_unit_vector(double *unit_vec_out) {
    // Coordinates of P and Q
    double **P = createMat(3,1) ;
    P[0][0] = 2; P[1][0] = 1; P[2][0] = -1;
    double **Q = createMat(3,1) ;
    Q[0][0] = 4; Q[1][0] = 4; Q[2][0] = -7;

    // Vector PQ = Q - P
    double **PQ = createMat(3,1);
    for (int i = 0; i < 3; i++) {
        PQ[i][0] = Q[i][0] - P[i][0];
    }

    // Magnitude of PQ
    double magnitude = Matnorm(PQ,3);

    // Unit vector along PQ
    double **unit_vec = createMat(3,1);

    for (int i = 0; i < 3; i++) {
        unit_vec[i][0] = PQ[i][0] / magnitude;
    }

    // Print the unit vector
    printf("Unit vector along PQ: (%.4f, %.4f, %.4f)\n", unit_vec[0][0], unit_vec[1][0], unit_vec[2][0]);
    

    unit_vec_out[0] = unit_vec[0][0];
    unit_vec_out[1] = unit_vec[1][0];    
    unit_vec_out[2] = unit_vec[2][0];

}

int main() {
    double unit_vec[3];
    get_unit_vector(unit_vec);
    return 0;
}