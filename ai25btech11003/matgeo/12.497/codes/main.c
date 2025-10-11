#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Faddeev–LeVerrier algorithm to compute the characteristic polynomial
// of an n×n matrix A. Writes coefficients for λ^n + a₁λ^(n−1) + ... + aₙ = 0
void compute_char_eq(int n, double *A, const char *out_filename) {
    double *B = malloc(n*n*sizeof(double));
    double *tmp = malloc(n*n*sizeof(double));
    double *trace = malloc((n+1)*sizeof(double));
    double *c = malloc((n+1)*sizeof(double));
    if (!B||!tmp||!trace||!c) { perror("Allocation failed"); return; }

    // B₀ = I
    memset(B,0,n*n*sizeof(double));
    for(int i=0;i<n;i++) B[i*n+i]=1.0;

    c[0]=1.0;
    for(int k=1;k<=n;k++){
        // tmp = A × Bₖ₋₁
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                double sum=0;
                for(int t=0;t<n;t++) sum += A[i*n+t]*B[t*n+j];
                tmp[i*n+j]=sum;
            }
        }
        // trace[k]
        trace[k]=0;
        for(int i=0;i<n;i++) trace[k] += tmp[i*n+i];
        c[k] = -trace[k]/k;
        // Bₖ = tmp + c[k]·I
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                B[i*n+j]=tmp[i*n+j] + (i==j ? c[k] : 0);
            }
        }
    }

    FILE *f = fopen(out_filename,"w");
    if(!f){ perror("File open failed"); }
    else {
        // Print λ^n + a₁λ^(n−1) + ... + aₙ = 0
        for(int k=0;k<=n;k++){
            double coef = c[n-k];
            if(k>0) fprintf(f, coef>=0 ? " + " : " - ");
            if(k==0) {
                fprintf(f, "1");
            } else {
                fprintf(f, "%.6g", fabs(coef));
                fprintf(f, "λ");
                if(n-k>1) fprintf(f, "^%d", n-k);
            }
        }
        fprintf(f," = 0\n");
        fclose(f);
    }

    free(B); free(tmp); free(trace); free(c);
}

int main(void) {
    // Matrix A from main.pdf: [3 2; 4 1]
    int n = 2;
    double A[4] = { 3, 2,
                    4, 1 };
    compute_char_eq(n, A, "main.dat");
    return 0;
}

