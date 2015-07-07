/* This file is automatically generated. DO NOT EDIT! */

#ifndef _explanesignoi_h
#define _explanesignoi_h


#include <rsf.h>


void explanesignoi_init (int m1,int m2 /* data size */, 
			 float eps1    /* signal/noise scaling */, 
			 float **aa    /* frequency filter [4][m1*m2] */, 
			 int nw        /* dip filter order */, 
			 int nj1       /* dip filter step for noise */, 
			 int nj2       /* dip filter step for signal */, 
			 float **nn    /* noise dip [m1*m2] */, 
			 float **ss    /* signal dip [m1*m2] */);
/*< initialize >*/


void explanesignoi_close(void);
/*< free allocated storage >*/


void explanesignoi_lop (bool adj, bool add, int ns, int nd, 
			float *ss, float *dat);
/*< linear operator for inversion >*/

#endif
