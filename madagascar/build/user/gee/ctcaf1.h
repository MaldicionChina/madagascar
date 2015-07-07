/* This file is automatically generated. DO NOT EDIT! */

#ifndef _ctcaf1_h
#define _ctcaf1_h


#include <rsf.h>


void ctcaf1_init(int ny         /* data size */, 
		sf_complex* yy /* data [ny] */);
/*< initialize >*/


void ctcaf1_lop(bool adj, bool add, int nb, int ny, sf_complex *bb, sf_complex *yy);
/*< linear operator >*/

#endif
