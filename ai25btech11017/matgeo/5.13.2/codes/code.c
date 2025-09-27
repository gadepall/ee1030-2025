#include<stdio.h>
int main(){
    int arr[2][2];
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    int arr2[2][2]={0};
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++){
            for(int z=0;z<2;z++){
                arr2[i][j]+=arr[i][z]*arr[z][j];
            }
        }
    }
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++){
            printf("%d",arr2[i][j]);
        }
        printf("\n");
    }
    return 0;
}