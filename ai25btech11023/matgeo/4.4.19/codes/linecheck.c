// linecheck.c
#include <stdio.h>

int point_on_line(int n1, int n2, int x, int y, int c) {
    // Implements n^T x = c, i.e., n1*x + n2*y == c
    return (n1 * x + n2 * y) == c;
}
