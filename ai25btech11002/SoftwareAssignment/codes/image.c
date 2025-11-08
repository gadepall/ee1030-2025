sorry this was the code:
#include <stdio.h>
#include <stdlib.h>
#include <png.h>
#include <math.h>
int main(){
png_structp png_ptr=png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL,NULL,NULL);
png_infop info_ptr=png_create_info_struct(png_ptr);
printf("Enter image name to convert to pgm:\n");
char s[100];
scanf("%s",s);
FILE *fp=fopen(s,"rb");
png_init_io(png_ptr, fp);
png_read_info(png_ptr,info_ptr);
int width=png_get_image_width(png_ptr,info_ptr);
int height=png_get_image_height(png_ptr,info_ptr);
int bitd=png_get_bit_depth(png_ptr,info_ptr);
int color_type=png_get_color_type(png_ptr,info_ptr);
png_bytep* row_pointers= (png_bytep*)malloc(sizeof(png_bytep)*height);
for(int i=0;i<height;i++){
row_pointers[i]=(png_byte*)malloc(width);
}
png_read_rows(png_ptr,row_pointers,NULL,height);
FILE *ofp = fopen("ogen.pgm","wb");
fprintf(ofp,"P2\n%d %d\n255\n",width,height);
for(int i=0;i<height;i++){
for(int j=0;j<width;j++){
fprintf(ofp,"%d ",row_pointers[i][j]);
}
fprintf(ofp,"\n");
}
fclose(ofp);
for(int i=0;i<height;i++){
free(row_pointers[i]);
}
free(row_pointers);
png_destroy_read_struct(&png_ptr,&info_ptr,NULL);
fclose(fp);
return 0;
}
