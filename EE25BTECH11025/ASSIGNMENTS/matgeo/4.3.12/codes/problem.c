#include<stdio.h>
#include<math.h>

void give_data(double *points){
    points[0] = 1; //Ax
    points[1] = -2; //Ay
    points[2] = 0; //Bx
    points[3] = 2; //By
    points[4] = 2; //Cx
    points[5] = 0; //Cy
    points[6] = 4; //Dx
    points[7] = 0; //Dy
    points[8] = sqrt(2); //EX
    points[9] = 4*sqrt(2); //Ey
    points[10] = 1; //Fx
    points[11] = 1; //Fy
}

double dotpro(double A[], double B[]){
    double sum = 0;
    for(int i = 0; i<2; i++){
        sum += (A[i]*B[i]);
    }
    return sum;
}
int main(){
    double n[2] = {1, -2};
    double A[2] = {0, 2};
    double B[2] = {2, 0};
    double C[2] = {4, 0};
    double D[2] = {sqrt(2), 4*sqrt(2)};
    double E[2] = {1, 1};
    int k = 0;

    for(int i = 1; i<=5; i++){
        switch (i){
            case 1: k = dotpro(n, A); if(k==4){printf("Option (%d) lies on the given line.", i);}
            else{printf("Option (%d) does not lie on the given line", i);}
            break;
            case 2: k = dotpro(n, B); if(k==4){printf("Option (%d) lies on the given line.", i);}
            else{printf("Option (%d) does not lie on the given line", i);}
            break;
            case 3: k = dotpro(n, C); if(k==4){printf("Option (%d) lies on the given line.", i);}
            else{printf("Option (%d) does not lie on the given line", i);}
            break;
            case 4: k = dotpro(n, D); if(k==4){printf("Option (%d) lies on the given line.", i);}
            else{printf("Option (%d) does not lie on the given line", i);}
            break;
            case 5: k = dotpro(n, E); if(k==4){printf("Option (%d) lies on the given line.", i);}
            else{printf("Option (%d) does not lie on the given line", i);}
            break;
        }
    }
}