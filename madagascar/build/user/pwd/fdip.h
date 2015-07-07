/* This file is automatically generated. DO NOT EDIT! */

#ifndef _fdip_h
#define _fdip_h


void fdip_init(int m1,int m2,int m3,int *rect, int niter, bool verb);
/*< initialize >*/


void fdip_close();
/*< release work space >*/


void fdip(float *in,float *out, 
	  bool **mask, /* input mask for known data */
	  int dim /* 0 - inline; 1 - xline; X - both*/);
/*< 3D dip estimation >*/

#endif
