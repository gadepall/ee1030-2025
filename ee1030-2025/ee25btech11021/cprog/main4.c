#include <stdio.h>

int main() {
    int n, i, count;
    printf("Enter a number: ");
    scanf("%d", &n);

    int temp = n;  // store original number

    printf("%d = ", temp);

    for (i = 2; i <= n; i++) {
        count = 0;
        while (n % i == 0) {   // check divisibility
            count++;
            n = n / i;
        }
        if (count > 0) {
            printf("%d^%d", i, count);
            if (n > 1) printf(" × "); // avoid extra × at the end
        }
    }

    return 0;
}
