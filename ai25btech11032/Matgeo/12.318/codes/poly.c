#include <stdio.h>

// Base factor polynomial f(x) = (x-1)(x-0.5)(x-5)(x-7)(x-3)(x-4)
double base_factor(double x) {
    return (x-1.0)*(x-0.5)*(x-5.0)*(x-7.0)*(x-3.0)*(x-4.0);
}

