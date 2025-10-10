#include <stdio.h>
#include <math.h>
double* compute_points_and_area() {
    static double results[5]; // results[0,1]=P1, [2,3]=P2, [4]=area

    double h[2] = {0, 6};
    double m[2] = {2, 3};
    double V[2][2] = {{3,0},{0,0}};
    double u[2] = {0, -2};
    double f = 0;

    // Step 1: V*h + u
    double Vh[2];
    Vh[0] = V[0][0]*h[0] + V[0][1]*h[1];
    Vh[1] = V[1][0]*h[0] + V[1][1]*h[1];

    double Vh_plus_u[2] = {Vh[0]+u[0], Vh[1]+u[1]};

    // Step 2: m^T*(Vh+u)
    double mT_Vh_plus_u = m[0]*Vh_plus_u[0] + m[1]*Vh_plus_u[1];

    // Step 3: m^T * V * m
    double Vm[2] = { V[0][0]*m[0] + V[0][1]*m[1], V[1][0]*m[0] + V[1][1]*m[1] };
    double mT_V_m = m[0]*Vm[0] + m[1]*Vm[1];

    // Step 4: g(h)
    double hT_V_h = h[0]*(V[0][0]*h[0]+V[0][1]*h[1]) + h[1]*(V[1][0]*h[0]+V[1][1]*h[1]);
    double uT_h = u[0]*h[0] + u[1]*h[1];
    double g_h = hT_V_h + 2*uT_h + f;

    // Step 5: kappa values
    double sqrt_term = sqrt(mT_Vh_plus_u*mT_Vh_plus_u - g_h*mT_V_m);
    double kappa1 = (-mT_Vh_plus_u + sqrt_term)/mT_V_m;
    double kappa2 = (-mT_Vh_plus_u - sqrt_term)/mT_V_m;

    // Step 6: Intersection points
    results[0] = h[0] + kappa1*m[0]; // P1 x
    results[1] = h[1] + kappa1*m[1]; // P1 y
    results[2] = h[0] + kappa2*m[0]; // P2 x
    results[3] = h[1] + kappa2*m[1]; // P2 y

    // Step 7: Area
    double x1 = results[2]; // -2
    double x2 = results[0]; // 4
    results[4] = fabs((1.0/4)*(pow(x2,3)-pow(x1,3)-3*(pow(x2,2)-pow(x1,2))-24*(x2-x1)));

    return results;
}
