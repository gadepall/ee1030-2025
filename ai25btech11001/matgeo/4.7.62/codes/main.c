#include<stdio.h>

struct Vec3{
		float x,y,z;
};


int dotVec3(struct Vec3 v1,struct Vec3 v2){
		//struct Vec2 v;
		return v1.x*v2.x+
				v1.y*v2.y+
				v1.z*v2.z;
}
