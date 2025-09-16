// 2.10.28  —  Check |(a×b)·c| = |a||b||c|  and options (a)-(d)
// Compile:  gcc sol_2_10_28.c -lm
#include <stdio.h>
#include <math.h>

typedef struct { double x, y, z; } V3;

static inline V3  cross(V3 a, V3 b){
    V3 c = { a.y*b.z - a.z*b.y,
             a.z*b.x - a.x*b.z,
             a.x*b.y - a.y*b.x };
    return c;
}
static inline double dot(V3 a, V3 b){ return a.x*b.x + a.y*b.y + a.z*b.z; }
static inline double norm(V3 a){ return sqrt(dot(a,a)); }
static inline int iszero(double t){ return fabs(t) < 1e-9; }

int main(void){
    V3 a, b, c;
    // Input: ax ay az  bx by bz  cx cy cz
    if (scanf("%lf %lf %lf %lf %lf %lf %lf %lf %lf",
              &a.x,&a.y,&a.z, &b.x,&b.y,&b.z, &c.x,&c.y,&c.z) != 9) return 0;

    double lhs = fabs(dot(cross(a,b), c));             // |(a×b)·c|
    double rhs = norm(a) * norm(b) * norm(c);          // |a||b||c|
    int eq = fabs(lhs - rhs) < 1e-9;

    int ab0 = iszero(dot(a,b));
    int bc0 = iszero(dot(b,c));
    int ca0 = iszero(dot(c,a));

    printf("|(a×b)·c| = %.10f\n", lhs);
    printf("|a||b||c| = %.10f\n", rhs);
    printf("Equality holds? %s\n\n", eq ? "YES" : "NO");

    printf("Option (a)  a·b=0 & b·c=0 : %s\n", (ab0 && bc0) ? "true":"false");
    printf("Option (b)  b·c=0 & c·a=0 : %s\n", (bc0 && ca0) ? "true":"false");
    printf("Option (c)  c·a=0 & a·b=0 : %s\n", (ca0 && ab0) ? "true":"false");
    printf("Option (d)  a·b=b·c=c·a=0 : %s\n", (ab0 && bc0 && ca0) ? "true":"false");

    // IFF check (geometric condition: a ⟂ b and c ∥ a×b ⇒ all three dot products zero)
    if (eq && !(ab0 && bc0 && ca0))
        puts("\nNote: For equality, a ⟂ b and c ∥ a×b, which forces a·b=b·c=c·a=0.");
    if (!eq && (ab0 && bc0 && ca0))
        puts("\nSince a ⟂ b and c ⟂ a,b, equality should hold (up to rounding).");

    return 0;
}
