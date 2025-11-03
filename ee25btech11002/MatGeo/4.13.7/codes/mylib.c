#include <stdio.h>
void line_coefficients(int a, int d, int coeffs[3]) {
    coeffs[0] = a;       
    coeffs[1] = a + d;   
    coeffs[2] = a + 2*d;
}