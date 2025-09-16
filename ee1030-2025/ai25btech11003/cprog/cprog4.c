#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main() {
    int num = -12, den = 18;

    int divisor = gcd(abs(num), abs(den));

    num /= divisor;
    den /= divisor;

    if (den < 0) {
        den = -den;
        num = -num;
    }

    printf("Standard form: %d/%d\n\n", num, den);
    return 0;
}

