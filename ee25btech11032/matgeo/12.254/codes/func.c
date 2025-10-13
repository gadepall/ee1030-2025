#include <math.h>
#include <complex.h>


complex double dot_product(double p , double q) {
    complex double a = p + I * (q);

    complex double v1[3] = {1.0, 1.0, 1.0};
    complex double v2[3] = {1.0, a, cpow(a, 2)};

    
    complex double ans = 0.0 + 0.0*I;
    for (int i = 0; i < 3; i++) {
        ans += v1[i] * v2[i];
    }

    
    if (fabs(creal(ans)) < 1e-10) ans -= creal(ans);
    if (fabs(cimag(ans)) < 1e-10) ans -= I * cimag(ans);

    return ans;
}
