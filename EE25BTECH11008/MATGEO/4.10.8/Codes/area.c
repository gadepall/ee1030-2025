#include <math.h>

double dot(double* x, double* y, int l) {
    double ans = 0;
    for (int i=0; i<l; i++) {
        ans += x[i]*y[i];
    }
    return ans;
}

double triangle_area(double m1, double c1, double m2, double c2) {
    double A[2] = {0, c1};
    double B[2] = {0, c2};
    
    double x = (c2 - c1) / (m1 - m2);
    double y = m1 * x + c1;
    double C[2] = {x, y};
    
    double u[2] = {B[0] - A[0], B[1] - A[1]};
    double v[2] = {C[0] - A[0], C[1] - A[1]};
    
    double cross = pow(dot(u, u, 2)*dot(v, v, 2) - pow(dot(u, v, 2), 2), 0.5);
    
    return 0.5 * fabs(cross);
}
