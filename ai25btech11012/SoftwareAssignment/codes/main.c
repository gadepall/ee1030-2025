#include<stdio.h>
#include<string.h>
#include<stdlib.h>

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
}}
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
 size_t read = fread(buff,1,(*r)*(*c),f);
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
int main()
{ int r,c;
  float **A = read("/Users/unnathi/Documents/ee1030-2025/ai25btech11012/SoftwareAssignment/figs/einstein.pgm",&r,&c);
  if(!A)
  {return 1;}
  free_matrix(A,r);
  return 0;
}
