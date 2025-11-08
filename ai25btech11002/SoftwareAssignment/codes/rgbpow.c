#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double norm(double *vec, int n) {
    double tot = 0.0;
    for (int i = 0; i < n; i++) tot += vec[i] * vec[i];
    return sqrt(tot);
}

void Ax(double *b, double *A, double *x, int m, int n) {
    for (int i = 0; i < m; i++) {
        b[i] = 0;
        for (int j = 0; j < n; j++)
            b[i] += A[i * n + j] * x[j];
    }
}

void A_Tx(double *b, double *A, double *x, int m, int n) {
    for (int i = 0; i < n; i++) {
        b[i] = 0;
        for (int j = 0; j < m; j++)
            b[i] += A[j * n + i] * x[j];
    }
}

void normalize(double *vec, int n) {
    double nrm = norm(vec, n);
    if (nrm < 1e-12) return;
    for (int i = 0; i < n; i++) vec[i] /= nrm;
}

void svd(double *A_src, int m, int n, int k, double *U, double *S, double *V) {
    double *A = (double *)malloc(m * n * sizeof(double));
    for (int i = 0; i < m * n; i++) A[i] = A_src[i];
    double *v = (double *)malloc(n * sizeof(double));
    double *u = (double *)malloc(m * sizeof(double));
    double *Av = (double *)malloc(m * sizeof(double));
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < n; j++) v[j] = (rand() / (double)RAND_MAX) - 0.5;
        normalize(v, n);
        for (int j = 0; j < 100; j++) {
            Ax(Av, A, v, m, n);
            A_Tx(v, A, Av, m, n);
            normalize(v, n);
        }
        Ax(Av, A, v, m, n);
        S[i] = norm(Av, m);
        for (int j = 0; j < m; j++) u[j] = Av[j] / S[i];
        for (int j = 0; j < m; j++) U[j * k + i] = u[j];
        for (int j = 0; j < n; j++) V[j * k + i] = v[j];
        for (int j = 0; j < m; j++)
            for (int p = 0; p < n; p++)
                A[j * n + p] -= S[i] * u[j] * v[p];
    }
    free(A);
    free(v);
    free(u);
    free(Av);
}

int main() {
    char s[100];
    printf("Enter filename to decompose:\n");
    scanf("%99s", s);
    srand(time(NULL));

    FILE *fp = fopen(s, "r");
    if (!fp) {
        printf("Cannot open file\n");
        return 1;
    }

    char format[3];
    int width, height, max_white;
    fscanf(fp, "%2s %d %d %d", format, &width, &height, &max_white);
    if (max_white == 0) max_white = 255;

    double *A = (double *)malloc(height * width * 3 * sizeof(double));
    int r, g, b, idx = 0;
    while (fscanf(fp, "%d %d %d", &r, &g, &b) == 3) {
        if (idx >= height * width * 3) break;
        A[idx++] = (double)r / max_white;
        A[idx++] = (double)g / max_white;
        A[idx++] = (double)b / max_white;
    }
    fclose(fp);

    double norm_A = 0.0;
    for (int i = 0; i < height * width * 3; i++) {
        double val = A[i];
        norm_A += val * val;
    }
    norm_A = sqrt(norm_A);

    int k_vals[] = {5, 20, 50, 100, 200, 500};
    int n_k = sizeof(k_vals) / sizeof(k_vals[0]);

    for (int idx_k = 0; idx_k < n_k; idx_k++) {
        int k = k_vals[idx_k];

        double *U = (double *)malloc(height * k * sizeof(double));
        double *S = (double *)malloc(k * sizeof(double));
        double *V = (double *)malloc(width * 3 * k * sizeof(double));
        double *A_copy = (double *)malloc(height * width * 3 * sizeof(double));
        for (int i = 0; i < height * width * 3; i++) A_copy[i] = A[i];

        clock_t start = clock();
        svd(A_copy, height, width * 3, k, U, S, V);
        clock_t end = clock();
        double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

        double *Ak = (double *)malloc(height * width * 3 * sizeof(double));
        for (int r = 0; r < height; r++)
            for (int c = 0; c < width * 3; c++) {
                double sum = 0.0;
                for (int t = 0; t < k; t++)
                    sum += U[r * k + t] * S[t] * V[c * k + t];
                Ak[r * width * 3 + c] = sum;
            }

        char out_name[64];
        snprintf(out_name, sizeof(out_name), "recon_%d.ppm", k);
        FILE *out = fopen(out_name, "w");
        fprintf(out, "P3\n%d %d\n255\n", width, height);
        for (int r = 0; r < height; r++) {
            for (int c = 0; c < width; c++) {
                int a0 = r * width * 3 + c * 3;
                int pr = (int)(Ak[a0] * 255.0 + 0.5);
                int pg = (int)(Ak[a0+1] * 255.0 + 0.5);
                int pb = (int)(Ak[a0+2] * 255.0 + 0.5);
                if (pr < 0) pr = 0;
                if (pr > 255) pr = 255;
                if (pg < 0) pg = 0;
                if (pg > 255) pg = 255;
                if (pb < 0) pb = 0;
                if (pb > 255) pb = 255;
                fprintf(out, "%d %d %d ", pr, pg, pb);
            }
            fprintf(out, "\n");
        }
        fclose(out);

        double err = 0.0;
        for (int i = 0; i < height * width * 3; i++) {
            double d = A[i] - Ak[i];
            err += d * d;
        }
        err = sqrt(err);
        double rel_err = norm_A > 1e-12 ? err / norm_A : 0.0;

        double orig_size = (double)(height * width * 3);
        double comp_size = (double)k * (height + width * 3 + 1);
        double comp_ratio = orig_size / comp_size;

        printf("k=%4d | ||A-A_k||_F=%.6f | RelErr=%.6f | CompRatio=%.2f:1 | Time=%.4fs\n",
               k, err, rel_err, comp_ratio, time_spent);

        free(U);
        free(S);
        free(V);
        free(Ak);
        free(A_copy);
    }

    free(A);
    return 0;
}
