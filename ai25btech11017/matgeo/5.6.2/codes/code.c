#include<stdio.h>
int main(){
    int arr[3][3];
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    int arr2[3][3]={0};
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            for(int z=0;z<3;z++){
                arr2[i][j]+=arr[i][z]*arr[z][j];
            }
        }
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            //printf("%d",arr2[i][j]);
            if(i==j){
                printf("%d ",arr2[i][j]-5*arr[i][j]+6);
            }
            else{
                printf("%d ",arr2[i][j]-5*arr[i][j]);
            }
        }
        printf("\n");
    }
    return 0;
}