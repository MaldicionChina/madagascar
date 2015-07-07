/* This file is automatically generated. DO NOT EDIT! */

#ifndef _npolydiv_h
#define _npolydiv_h


#include <rsf.h>


#include "nhelix.h"


void npolydiv_init (int nd_in     /* data size */, 
		    nfilter aa_in /* filter */);
/*< initialize >*/


void npolydiv_close(void);
/*< free allocated storage >*/


void npolydiv_lop (bool adj, bool add, int nx, int ny, float *xx, float *yy);
/*< linear operator >*/

#endif
