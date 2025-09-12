#include <stdio.h>
#include <math.h>

int main() {
    int qx = 0, qy = 1;
    int px = 5, py = -3;
    int ry = 6;
    // Distance QP^2
    int dQP2 = (qx - px) * (qx - px) + (qy - py) * (qy - py);
    // Equation: (qx - x)^2 + (qy - ry)^2 = dQP^2
    // => (0 - x)^2 + (1 - 6)^2 = dQP2
    // => x^2 + 25 = dQP2
    int rhs = dQP2 - 25;
    int x1 = (int)sqrt(rhs);
    int x2 = -x1;
     printf("The value of x can be %d or %d\n", x1, x2);
    return 0;
}