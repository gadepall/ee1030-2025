// main.c
// Compile: gcc -shared -o libsolver.so -fPIC main.c -lm

#include <stdio.h>

typedef struct {
    double x;
    double y;
} Point;

typedef struct {
    Point sols[2];
    int count;
} SolutionSet;

// Solve 6x+3y=6xy, 2x+4y=5xy
SolutionSet solve_equations() {
    SolutionSet S;
    S.count = 0;

    // Solution 1: (0,0)
    S.sols[S.count].x = 0;
    S.sols[S.count].y = 0;
    S.count++;

    // Solution 2: (1,2)
    S.sols[S.count].x = 1;
    S.sols[S.count].y = 2;
    S.count++;

    return S;
}

#ifdef TEST_C
int main(){
    SolutionSet S = solve_equations();
    for(int i=0; i<S.count; i++){
        printf("Solution %d: (%.2f, %.2f)\n", i+1, S.sols[i].x, S.sols[i].y);
    }
    return 0;
}
#endif

