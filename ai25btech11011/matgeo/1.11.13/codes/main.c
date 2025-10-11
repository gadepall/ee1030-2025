#include <stdio.h>

void find_direction_cosines(int alpha_deg, int beta_deg, int gamma_deg, double *l, double *m, double *n);

int main(){
    double l, m, n;
    find_direction_cosines(90, 135, 45, &l, &m, &n);
    printf("Direction cosines:\nl = %.4lf\nm = %.4lf\nn = %.4lf\n", l, m, n);
    return 0;
}

