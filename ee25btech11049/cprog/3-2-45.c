#include <stdio.h>
int main(void) {
    float a = -5.0 / -9.0;
    float b =  5.0 / -9.0;
    printf("a = %f\n", a);
    printf("b = %f\n", b);

    if (a > b) {
        printf("a is greater than b\n");
    } else if (a < b) {
         printf("a is less than b\n");
    } else {
        printf("a is equal to b\n");
    }
    return 0;
}
