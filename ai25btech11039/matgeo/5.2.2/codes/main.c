
#include <stdio.h>

static long long llabsll(long long x){ return x < 0 ? -x : x; }
static long long gcdll(long long a, long long b){
    a = llabsll(a); b = llabsll(b);
    while (b){ long long t = a % b; a = b; b = t; }
    return a ? a : 1;
}

int main(void){
    /* Integers for exact arithmetic */
    long long a11 = 5,  a12 = -4;
    long long a21 = 7,  a22 =  6;
    long long b1  = -8, b2  =  9;

    /* Determinants */
    long long detA   = a11*a22 - a12*a21;          /* 5*6 - (-4)*7 = 58 */
    long long det_u  = b1 *a22 - a12*b2;           /* (-8)*6 - (-4)*9 = -12 */
    long long det_v  = a11*b2  - b1 *a21;          /* 5*9  - (-8)*7   = 101 */

    if(detA == 0){
        puts("System is singular (no unique solution).");
        return 0;
    }

    /* Reduce fractions */
    long long g1 = gcdll(det_u, detA);
    long long g2 = gcdll(det_v, detA);
    long long un = det_u/g1, ud = detA/g1;         /* u = un/ud */
    long long vn = det_v/g2, vd = detA/g2;         /* v = vn/vd */

    /* Decimal forms */
    double u = (double)det_u / (double)detA;
    double v = (double)det_v / (double)detA;

    printf("Solution (fractions):  u = %lld/%lld,  v = %lld/%lld\n", un, ud, vn, vd);
    printf("Solution (decimals):   u = %.10f, v = %.10f\n", u, v);

    return 0;
}
