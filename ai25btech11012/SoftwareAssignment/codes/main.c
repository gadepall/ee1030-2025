#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

#define MAX 500


float **matrix(int r,int c)
{
   float **m = malloc(r*sizeof(float*));
   if(!m)
  {
    exit(1);
  }
   for(int i = 0;i<r;i++)
   {
   m[i] = malloc(c*sizeof(float));
    if(!m[i])
    {
     exit(1);
    }
   }
  return m;
}
void free_matrix(float **m,int r)
{
  for(int i =0;i<r;i++)
  {
   free(m[i]);
   }
  free(m);
}

float **read(const char *file , int *r,int *c)
{
  FILE *f = fopen(file,"rb");
  if(!f)
  {
   printf("Error opening the file");
   return NULL;
  }
 char m[3];
  if(!fgets(m,sizeof(m),f))
  {
   fclose(f);
   return NULL;
  }
 int ch;
 while((ch = fgetc(f))== '#')
  {
    while(fgetc(f) != '\n');
  }
  ungetc(ch,f);
  int max;
  fscanf(f,"%d %d",c,r);
  fscanf(f,"%d",&max);
  fgetc(f);

  float **A = matrix(*r,*c);
  unsigned char *buff = malloc((*r)*(*c));
  size_t readd = fread(buff,1,(*r)*(*c),f);
  fclose(f);
 int id = 0 ;
  for(int i=0;i<*r;i++)
  {
   for(int j = 0;j<*c;j++)
    {
     A[i][j] = (float)buff[id++];
    }
   }
  free(buff);
  return A;
}

float **alloc(int r,int c)
{
  float **m = malloc(r*sizeof(float*));
  for(int i =0;i<r;i++)
  {
  m[i] = calloc(c,sizeof(float));
  }
  return m;
}

float ** mult(float **A,float **B,int m,int n,int p)
{
 float **C = alloc(m,p);
 for(int i = 0;i<m;i++)
 {
  for(int j =0;j<p;j++)
  {
   float s = 0.0f;
   for(int k =0;k<n;k++)
    {
     s += A[i][k]*B[k][j];
    }
   C[i][j] = s;
  }
 }
 return C;
}


float **transpose(float **A,int r,int c)
{
 float **T = alloc(c,r);
 for(int i =0;i<r;i++)
  {
   for(int j = 0 ;j<c;j++)
   {
     T[j][i] = A[i][j];
   }
  }
  return T;
}

void normal(float *v,int n)
{
 float norm = 0.0f;
 for(int i =0;i<n;i++)
 {
  norm += v[i]*v[i];
 }
 norm = sqrtf(norm);
 for(int i= 0;i<n;i++)
 { 
	 v[i] /= (norm);
  }
}

float ite(float **A,int n,float *v)
{
  float *tmp = calloc(n,sizeof(float));
  for(int it =0;it<MAX;it++)
  {
   for(int i =0;i<n;i++)
   {
    tmp[i] = 0.0f;
    for(int j =0;j<n;j++)
    {
      tmp[i] +=A[i][j]*v[j];
    }
   }
   normal(tmp,n);
   float d = 0.0f;
   for(int i =0;i<n;i++)
   {
    d += fabsf(tmp[i] - v[i]);
   }
   if(d<1e-6)
   {break;}
   for(int i =0;i<n;i++)
   {
    v[i] = tmp[i];
   }
  }
 
  float l =0.0f;
  for(int i =0;i<n;i++)
  {
   float Av = 0.0f;
   for(int j =0;j<n;j++)
   {
    Av += A[i][j]*v[j];
   }
  l += v[i]*Av;
  }
  free(tmp);
  return l;

}

void eigen(float **A,int n,float **evec,float *evals)
{
  for(int k =0;k<n;k++)
  {
   float *v = calloc(n,sizeof(float));
   for(int i =0;i<n;i++)
   {
    v[i] = rand()/(float)RAND_MAX;
   }
   normal(v,n);
   
  float l = ite(A,n,v);
  evals[k] = l;

  for(int i =0;i<n;i++)
  {
   evec[i][k] = v[i];
  }

  for(int i =0;i<n;i++)
  {
   for(int j=0;j<n;j++)
   {
    A[i][j] -= l*v[i]*v[j];
   }
  }
 free(v);
  }

}

void svd(float **A,int r,int c,float **U,float *S,float **V)
{
  float **AT = transpose(A,r,c);
  float **ATA = mult(AT,A,c,r,c);
  float **evec = alloc(c,c);
  float *evals = calloc(c,sizeof(float));
  eigen(ATA,c,evec,evals);

  for(int i= 0;i<c-1;i++)
  { 
	  for(int j = i+1;j<c;j++)
	  {
		  if(evals[j]>evals[i])
		  {
		   float tmp = evals[i];
		   evals[i] = evals[j];
		   evals[j] = tmp;
		   for(int k =0;k<c;k++)
		   {
		    float t = evec[k][i];
		   evec[k][i] = evec[k][j];
		   evec[k][j] = t;}
		  }
	  }
   }
  for(int i =0;i<c;i++)
  {
   S[i] = sqrtf(fmaxf(evals[i],0.0f));
  }
  for(int i =0;i<c;i++)
  {
    for(int j =0;j<c;j++)
    {
     V[i][j] = evec[i][j];
    }
  }

  float **AV = mult(A,V,r,c,c);
  for(int i=0;i<r;i++)
  {
  for(int j =0;j<c;j++)
   { if(S[j]>1e-8)
	   {
	    U[i][j] = AV[i][j]/S[j];
	   }
     else
     {
      U[i][j] = 0.0f;}
    
  }
  }
  free_matrix(AT,c);
  free_matrix(ATA,c);
  free_matrix(evec,c);
  free(evals);
  free_matrix(AV,r);

}

float **rank(float **U,float *S,float **V,int r,int c,int k)
{
  if(k>c) k =c;
  float **Uk = alloc(r,k);
  float **Vk = alloc(c,k);
  float **Sig = alloc(k,k);
  for(int i=0;i<r;i++) 
  {
    for(int j =0;j<k;j++)
    { Uk[i][j] = U[i][j];
    }
  }
  for(int i =0;i<c;i++)
  {
   for(int j =0;j<k;j++)
   {
    Vk[i][j] = V[i][j];
   }
  }
  for(int i =0;i<k;i++)
  {
   Sig[i][i] = S[i];
  }
  float **US = mult(Uk,Sig,r,k,k);
  float **Vk_T = transpose(Vk,c,k);
  float **Ak = mult(US,Vk_T,r,k,c);

  free_matrix(Uk,r);
  free_matrix(Vk,c);
  free_matrix(Sig,k);
  free_matrix(US,r);
  free_matrix(Vk_T,k);
  return Ak;
}

float error(float **A,float **B,int m,int n)
{
  double s = 0.0;
  for(int i =0;i<m;i++)
  {
   for(int j =0;j<n;j++)
    {
     double d = (double)A[i][j] - (double)B[i][j];
    s += d*d;
    }
  }
  return (float)sqrt(s);
  
}

void pgm(const char *file,float **A,int r,int c)
{
 FILE *f = fopen(file,"wb");
 fprintf(f,"P5\n%d %d\n255\n",c,r);
 for(int i = 0;i<r;i++)
 {
  for(int j =0;j<c;j++)
   {
    float v= A[i][j];
    if(v<0.0f)
    {v = 0.0f;}
    else if(v>255.0f)
    {v = 255.0;}
    unsigned char b = (unsigned char)(v+0.5f);
    fwrite(&b,1,1,f);
   }}
 fclose(f);
}


int main()
{ 
  int r,c;
  float **A = read("/Users/unnathi/Documents/ee1030-2025/ai25btech11012/SoftwareAssignment/figs/einstein/einstein.pgm",&r,&c);
  if(!A)
   {return 1;}

  float **U = alloc(r,c);
  float *S = calloc(c,sizeof(float));
  float **V = alloc(c,c);

  svd(A,r,c,U,S,V);
  int k[] = {5,20,50,100};
  int nk = sizeof(k)/sizeof(k[0]);
   for(int i =0;i<nk;i++)
   {
   int K = k[i];
   float **Ak = rank(U,S,V,r,c,K);
   char name[64];
   sprintf(name,"einsteinreconstructedk_%d.pgm",K);
   pgm(name,Ak,r,c);
   float e = error(A,Ak,r,c);
   printf("k = %d Forbenius error = %.4f\n",K,e);
   free_matrix(Ak,r);
   }
  free_matrix(U,r);
  free_matrix(V,c);
  free(S);
  free_matrix(A,r);
  return 0;
}
