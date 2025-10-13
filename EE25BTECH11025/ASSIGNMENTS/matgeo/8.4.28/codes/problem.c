 #include<stdio.h>
 #include<math.h>

 double normf;
 double normv;
 double dvectora[2] = {1,1};
 double m1 = 1;

 double norm(double arr1[2]){
    double sum = 0;
    for(int i = 0; i<2; i++){
        sum+=(sqrt(arr1[i]*arr1[i]));
    }
    return sum;
}

double vdotv(double arr1[2], double arr2[2]){
    double sum = 0;
    for(int i = 0; i<2; i++){
        sum+=(arr1[i]*arr2[i]);
    }
    return sum;
}

void vplusv(double t, double v1[2], double v2[2], double P[2]){
    if(t==1){
        for(int i = 0; i<2; i++){
            P[i]=v1[i]+v2[i];
        }
    }
    if(t==-1){
        for(int i = 0; i<2; i++){
            P[i]=v1[i]-v2[i];
        }
    }
}

void give_data(double *points){

    normf = 2*sqrt(2); normv = sqrt(2);
    double lambda;
    lambda =(normf/norm(dvectora));
    double vectorF[2];
    for(int i = 0; i<2; i++){
        vectorF[i] = lambda*dvectora[i];
    }
    lambda = (normv/norm(dvectora));
    double vectorV[2];
    for(int i = 0; i<2; i++){
        vectorV[i] = lambda*dvectora[i];
    }
    double m2 = -1/m1;
    double dvectorb[2] = {1, m2};
    double X[2] = {2*vectorV[0], 2*vectorV[1]};
    double P[2];
    vplusv(1, X, vectorF, P);
    double c;
    double n[2]={0};
    double imp[2][2] = {{0, 1},{-1, 0}};
    for(int i = 0; i<2; i++){
        for(int j = 0; j<2; j++){
            n[i]+=imp[i][j]*dvectora[j];
        }
    }
    c = vdotv(n, P);
     points[0] = -8;
     points[1] = -2;
     points[2] = 16;
}
