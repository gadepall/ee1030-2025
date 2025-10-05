// Save as code.c and compile with: gcc -shared -o libregression.so -fPIC code.c
#include <stdio.h>

void get_data(double *years, double *production, int *n) {
    // Fill arrays with dataset, n=6
    double local_years[6] = {2001, 2002, 2003, 2004, 2005, 2006};
    double local_prod[6] = {30, 35, 36, 32, 37, 40};
    for(int i=0; i<6; i++) {
        years[i] = local_years[i];
        production[i] = local_prod[i];
    }
    *n = 6;
}

void get_stats(double *years, double *production, int n, double *out) {
    // Linear regression using normal equations, years mapped to 1,2,...,6
    double xsum=0, ysum=0, x2sum=0, xysum=0;
    for(int i=0; i<n; i++) {
        double x = i+1;
        double y = production[i];
        xsum += x;
        ysum += y;
        x2sum += x*x;
        xysum += x*y;
    }
    double beta = (n*xysum - xsum*ysum) / (n*x2sum - xsum*xsum);
    double alpha = (ysum - beta*xsum) / n;
    out[0] = alpha;
    out[1] = beta;
    out[2] = alpha + beta;
}

