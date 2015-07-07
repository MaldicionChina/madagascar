/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_multidivn_h
#define _sf_multidivn_h


#include "helix.h"


void sf_multidivn_init(int nw       /* number of components */, 
		       int ndim     /* number of dimensions */, 
		       int n        /* data size */, 
		       int *ndat    /* data dimensions [ndim] */, 
		       int *nbox    /* smoothing radius [ndim] */,
		       float* den   /* denominator [nw*nd] */,
		       sf_filter aa /* data filter */,
		       bool verb    /* verbosity flag */);
/*< initialize >*/


void sf_multidivn_close (void);
/*< free allocated storage >*/


void sf_multidivn (float* num  /* numerator */, 
		   float* rat  /* ratio */, 
		   int niter   /* number of iterations */);
/*< smoothly divide num/rat >*/

#endif
