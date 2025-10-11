#include <stdio.h>
int dot_product(int a[2], int b[2]) {
return a[0]*b[0] + a[1]*b[1];
}
int is_orthogonal(int a[2], int b[2]) {
return dot_product(a, b) == 0;
}
double line_equation(double x) {
return (3.0 - 2.0*x);
}
