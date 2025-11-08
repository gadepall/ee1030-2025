#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define STB_IMAGE_IMPLEMENTATION
#include "../c_libs/stb_image.h"

double **createMat(int m, int n)//creates a matrix of mxn
{
    double** y = (double** )malloc(m * sizeof(double *));
    for (int j = 0; j < m; j++)
        y[j] = (double *)calloc(n, sizeof(double));
    return y;
}

void freeMat(double **M, int rows)//free malloc
{
    for (int i = 0; i < rows; i++)
        free(M[i]);
    free(M);
}

double InnerProduct(double *a, double *b, int n)//computes innerproduct of a and b
{
    double ip = 0;
    for (int i = 0; i < n; i++)
        ip += a[i] * b[i];
    return ip;
}

double norm(double *a, int n)//computes norm of a
{
    return sqrt(InnerProduct(a, a, n));
}

void matMul(double** a, double** b, double **c, int m, int n, int l)//multiplies two matrices a and b and stores in c
{
    for (int i = 0; i < m; i++)
        for (int j = 0; j < l; j++)
        {
            double sum = 0;
            for (int k = 0; k < n; k++)
               sum += a[i][k] * b[k][j];
            c[i][j] = sum;
        }
}

void SVD(double** a, int m, int n, int k, double** U, double* S, double** V)//power iteration with deflation
{
    srand(time(NULL));
    double **Ac = createMat(m, n);
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            Ac[i][j] = a[i][j];		//Ac: a copy to compute svd
    
    for (int rank = 0; rank < k; rank++)
    {
        double *v = (double *)malloc(n * sizeof(double));
        for (int i = 0; i < n; i++)
            v[i] = (double)rand() / RAND_MAX - 0.5;  //generating a random matrix of nx1
        
        double *u = (double *)malloc(m * sizeof(double));
        
        for (int iter = 0; iter < 50; iter++)//power iteration
        {
            for (int i = 0; i < m; i++)
            {
                u[i] = 0;
                for (int j = 0; j < n; j++)
                    u[i] += Ac[i][j] * v[j];//u=Av_t-1
            }
            
            for (int j = 0; j < n; j++)
            {
                v[j] = 0;
                for (int i = 0; i < m; i++)
                    v[j] += Ac[i][j] * u[i];	//v=A^Tu_t
            }
            
            double nv = norm(v, n);
            if (nv < 1e-14) break;
            for (int j = 0; j < n; j++)
                v[j] /= nv;// v_t / ||v_t||
        }
        
        for (int i = 0; i < m; i++)
        {
            u[i] = 0;
            for (int j = 0; j < n; j++)
                u[i] += Ac[i][j] * v[j];//ur=Avr
        }
        
        double sigma = norm(u, m);
        S[rank] = sigma;
        
        if (sigma > 1e-14)
        {
            for (int i = 0; i < m; i++)
                u[i] /= sigma;//update u
        }
        
        for (int i = 0; i < m; i++)
            U[i][rank] = u[i];
        for (int j = 0; j < n; j++)
            V[j][rank] = v[j];
        
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                Ac[i][j] -= sigma * u[i] * v[j];
        
        free(u);
        free(v);
    }
    
    freeMat(Ac, m);
}
double **readimg(char *s, int *h, int *w)//input image
{
	int n;
	unsigned char *img = stbi_load(s, w, h, &n, 1);
	if(!img)
	{
		printf("Cannot load image\n");
		exit(1);
	}
	double **a = createMat(*h, *w);//stores pixels of image in matrix a
	for (int i = 0; i < *h; i++)
		for (int j = 0; j < *w; j++)
		a[i][j] = img[i * (*w) + j];
	stbi_image_free(img);
	return a;
}

void writePGM(double **a, int m, int n,char *o)//produces output as .pgm
{
	FILE *f = fopen(o, "w");
	fprintf(f, "P2\n");
	fprintf(f, "%d %d\n", n, m);
	fprintf(f, "255\n");
    
	for(int i = 0; i < m; i++)
	{
		for(int j = 0; j < n; j++)
		{
			int pixel = (int)(a[i][j] + 0.5); 
			if (pixel < 0) pixel = 0;
			if (pixel > 255) pixel = 255;
            
			fprintf(f, "%d", pixel);
			if (j < n - 1)
                	fprintf(f, " ");  
        	}
		fprintf(f, "\n");  
	}
    
	fclose(f);
	printf("Saved %s\n",o);
}

int main()
{
	FILE *p=fopen("input.txt","r");
	int h, w, k;
	char s[100],op[100];
	fscanf(p,"%s",s);
	fscanf(p,"%d", &k);
	fscanf(p,"%s",op);
	clock_t time;//to calculate runtime of program
	time=clock();
	double **A = readimg(s, &h, &w);
	int m = h, n = w;

	double **U = createMat(m, k);
	double *S = (double *)malloc(k * sizeof(double));
	double **V = createMat(n, k);
    
	SVD(A, m, n, k, U, S, V);
    
	double **Y = createMat(m, n);
	for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
        {
            double sum = 0;
            for (int r = 0; r < k; r++)
                sum += U[i][r] * S[r] * V[j][r];
            Y[i][j] = sum;
        }

	writePGM(Y, m, n,op);
	time=clock()-time;
	printf("Time required: %f seconds\n",(float)time / CLOCKS_PER_SEC);

	double f=0.0,fa=0.0;
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
		{
			f+=(A[i][j]-Y[i][j])*(A[i][j]-Y[i][j]);
			fa+=A[i][j]*A[i][j];
		}
	f=sqrt(f);
	fa=sqrt(fa);
	printf("Frobenius error : %lf\n",f);
	printf("Relative error : %lf%%\n",(f/fa)*100);
	freeMat(A, m);
	freeMat(U, m);
	free(S);
	freeMat(V, n);
	freeMat(Y, m);

	return 0;
}
