#include<stdio.h>

int check(double input, int t){
    double matB[2][2] = {{1, 0}, {5, 1}};
    double matA2[2][2];
    matA2[0][0] = input*input;
    matA2[0][1] = 0;
    matA2[1][0] = input + 1;
    matA2[1][1] = 1;
    int k = 1;
    for(int i = 0; i<2; i++){
        for(int j = 0; j<2; j++){
            if(matA2[i][j]==matB[i][j]){
                continue;
            }
            else{
                k = 0;
                break;
            }
        }
        if(k==0){
            break;
        }
    }
    
    if(k==0){
        printf("Given alpha = %.2lf is not the solution\n", input);
        t++;
    }
    else if(k==1){
        printf("Given alpha = %.2lf is the solution\n", input);
    }
    return t;

}

int main(){
    double input[3] = {1, 2, 4};
    int t = 0;
    int k = 0;
    for(int i = 0; i<3; i++){
        t = k; 
    k = check(input[i], t);
    }
    if(t==2){
        printf("only solution for the given question is alpha = infinity");
    }

}
