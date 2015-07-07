/* This file is automatically generated. DO NOT EDIT! */

#ifndef _spline_h
#define _spline_h


typedef struct{
	int n;
	const float *x,*f; /* [n]   data f(x)    */
	float *a,*b,*c,*d; /* [n-1] coefficients */
	bool linear;       /* linear or cubic    */
} Spl;


Spl *spline_init(const float *ff, /* [n] */
				 const float *xx, /* [n] sorted */
				 int nn,
				 bool linear);
/*< initialize >*/


void spline_eval(/*@out@*/ float *g, /* [m] */
				 const float *y,     /* [m] sorted */
				 int m,
				 const Spl *spl);
/*< evaluate >*/


void spline_free(Spl *spl);
/*< clean >*/

#endif
