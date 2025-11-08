#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
	int rows,cols,ch;
	printf("Enter the name of rgb image:\n");
	char s[100];
	scanf("%s",s);
	unsigned char* img=stbi_load(s,&cols,&rows,&ch,0);
	FILE *fp=fopen("rgbogen.ppm","w");
	fprintf(fp,"P3\n%d %d\n255\n",cols,rows);

    	for (int i=0;i<rows;i++) {
        	for (int j=0;j<cols;j++) {
			int idx=(i*cols+j)*ch;
			int r=img[idx];
			int g=img[idx+1];
			int b=img[idx+2];
			fprintf(fp,"%d %d %d ",r,g,b);
		}
		fprintf(fp,"\n");
	}
	fclose(fp);
	stbi_image_free(img);
	printf("Successful conversion\n");
	return 0;
}
