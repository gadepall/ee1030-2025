

#include <stdio.h>
#include <math.h>

typedef struct { double a, b; } Vec2;

/* reflect a point Q across the line n^T x = c (n != 0) */
static Vec2 reflect(Vec2 Q, Vec2 n, double c) {
    double nn = n.a*n.a + n.b*n.b;
    double alpha = 2.0 * ((n.a*Q.a + n.b*Q.b) - c) / nn;
    Vec2 R = { Q.a - alpha*n.a, Q.b - alpha*n.b };
    return R;
}

int main(void) {
    /* mirror line in vector form: n^T x = c with n = (1,-1), c = 0  => y = x */
    Vec2 n = {1.0, -1.0};
    double c = 0.0;

    printf("Mirror line (vector form): [1  -1] x = 0\n");
    printf("Mirror line (scalar form):  y = x\n\n");

    /* quick verification on a few t>0:
       Q(t) = (t, log10(t))  should reflect to R(t) = (log10(t), t) */
    double tests[] = {0.2, 0.5, 2.0, 10.0};
    for (int i = 0; i < 4; ++i) {
        double t = tests[i];
        Vec2 Q = { t, log10(t) };
        Vec2 R = reflect(Q, n, c);
        printf("t=%6.2f : Q=(%8.4f,%8.4f)  -->  R=(%8.4f,%8.4f)\n",
               t, Q.a, Q.b, R.a, R.b);
    }
    return 0;
}
