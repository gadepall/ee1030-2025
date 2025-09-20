// main.c
#include <stdio.h>
#include <math.h>

// Ellipse: center (h,k)=(-1,0), a=2, b=√3
static double e_h = -1.0, e_k = 0.0, e_a = 2.0, e_b = 1.7320508075688772;

// Parabola: vertex (h,k)=(-3,0), p=2
static double p_h = -3.0, p_k = 0.0, p_p = 2.0;

// Hyperbola: center (h,k)=(-9,0), a=6, b=√45
static double h_h = -9.0, h_k = 0.0, h_a = 6.0, h_b = 6.708203932499369;

// Exported functions
int get_ellipse_params(double *params) {
    params[0]=e_h; params[1]=e_k; params[2]=e_a; params[3]=e_b;
    return 0;
}
int get_parabola_params(double *params) {
    params[0]=p_h; params[1]=p_k; params[2]=p_p;
    return 0;
}
int get_hyperbola_params(double *params) {
    params[0]=h_h; params[1]=h_k; params[2]=h_a; params[3]=h_b;
    return 0;
}

int main() {
    FILE *f = fopen("main.dat", "w");
    // ellipse: h k a b
    fprintf(f, "%f %f %f %f\n", e_h, e_k, e_a, e_b);
    // parabola: h k p
    fprintf(f, "%f %f %f\n", p_h, p_k, p_p);
    // hyperbola: h k a b
    fprintf(f, "%f %f %f %f\n", h_h, h_k, h_a, h_b);
    fclose(f);
    return 0;
}

