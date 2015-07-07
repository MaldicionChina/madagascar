/* This file is automatically generated. DO NOT EDIT! */

#ifndef _icaf1_h
#define _icaf1_h


void icaf1_init (int ny    /* filter length */, 
		 float* yy /* data [nx] */, 
		 int lag1  /* filter lag (lag=1 is causal) */);
/*< initialize >*/


void icaf1_lop (bool adj, bool add, int nb, int ny, float* bb, float* yy);
/*< linear operator >*/

#endif
