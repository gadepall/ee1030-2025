#include <stdio.h>

int main() {
    float son, sumit;

    // Problem:
    // Sumit is 3 times as old as his son
    // => sumit = 3 * son
    //
    // After 5 years:
    // sumit + 5 = 2.5 * (son + 5)

    // Substituting sumit = 3 * son:
    // 3*son + 5 = 2.5*(son + 5)
    // 3*son + 5 = 2.5*son + 12.5
    // 0.5*son = 7.5
    // son = 15
    // sumit = 45

    son = (12.5f - 5.0f) / (3.0f - 2.5f);   // solving step
    sumit = 3 * son;

    printf("Son's present age = %.0f years\n", son);
    printf("Sumit's present age = %.0f years\n", sumit);

    return 0;
}

