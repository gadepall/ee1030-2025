#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
	char Iname[100];
	printf("Enter pgm file name:\n");
	scanf("%s",Iname);
	printf("Is data already written?[y/N]\n");
	char c='N';
	scanf(" %c",&c);
	if(c=='N'){
	FILE *fp=fopen(Iname,"w");
	if(fp==NULL)
		return -1;
	int m=5;
	int n=5;
	int white_max=15;
	printf("\nEnter dimensions:\n");
	scanf("%d %d",&m,&n);
	printf("Enter white pixel value(maximum value):\n");
	scanf("%d",&white_max);
	fprintf(fp,"P2\n");
	fprintf(fp,"%d %d\n",m,n);
	fprintf(fp,"%d\n",white_max);

	printf("Enter pixels for a %d x %d matrix where maximum value is %d:\n",m,n,white_max);
	int **pixels = malloc(m * sizeof(int *));
	for(int i=0;i<m;i++){
        pixels[i] = malloc(n * sizeof(int));
		for(int j=0;j<n;j++)
			scanf("%d",&pixels[i][j]);
	}
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++)
			fprintf(fp,"%d ",pixels[i][j]);
		fprintf(fp,"\n");
	}
        free(pixels);
	fclose(fp);
	printf("File creation suceeded.\n");
	}
	char command[100];
	strcpy(command,"xdg-open ");
	strcat(command,Iname);
	system(command);
	return 0;
}

