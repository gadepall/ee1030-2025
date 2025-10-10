#include <stdbool.h>

bool is_collinear(int a) {
    int det = 6 - 2*a;  // determinant
    return (det == 0);
}
