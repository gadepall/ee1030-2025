#include <stdio.h>

int main() {
    double k;

    printf("Enter value of k: ");
    scanf("%lf", &k);

    if (k == 5) {
        printf("Case A: Lines are concurrent (all meet at one point).\n");
    }
    else if (k == -6.0/5.0) {
        printf("Case B: One line is parallel to another.\n");
    }
    else if (k == 9 || k == 5.0/6.0) {
        printf("Case C: Lines form a triangle.\n");
    }
    else {
        printf("Case D: Lines do not form a triangle.\n");
    }

    return 0;
}
