#include <stdio.h>
int rank(int m,int n,float a[m][n]) {
   
    for (int i=0;i<m-1;i++){
	if (a[i][i] == 0) {
            for (int k=i+1; k<m; k++) {
                if (a[k][i] != 0) {
                    for (int j=0;j<n;j++) {
                        float tmp=a[i][j];
                        a[i][j]=a[k][j];
                        a[k][j]=tmp;
                    }
                    break;
                }
            }
        }
        float pivot=a[i][i];
        if (pivot==0)
            continue;
        for (int l=i;l<m-1;l++) {
            float k=a[l+1][i]/pivot;
            for(int j=0;j<n;j++) {
                a[l+1][j]-=a[i][j]*k;
            }
        }
    }
    int t=0;
    for(int i=0;i<m && i<n;i++){
      if(a[i][i]==0)
        t++;
    }
    if(m<n)
      return m-t;
    else
      return n-t;
}
