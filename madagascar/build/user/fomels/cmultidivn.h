/* This file is automatically generated. DO NOT EDIT! */

#ifndef _cmultidivn_h
#define _cmultidivn_h


void cmultidivn_init(int nw            /* number of components */, 
		       int ndim          /* number of dimensions */, 
		       int n             /* data size */, 
		       int *ndat         /* data dimensions [ndim] */, 
		       int *nbox         /* smoothing radius [ndim] */,
		       sf_complex* den   /* denominator [nw*nd] */,
		       bool verb         /* verbosity flag */);
/*< initialize >*/


void cmultidivn_close (void);
/*< free allocated storage >*/


void cmultidivn (sf_complex* num  /* numerator */, 
		 sf_complex* rat  /* ratio */, 
		 int niter        /* number of iterations */);
/*< smoothly divide num/rat >*/

#endif
