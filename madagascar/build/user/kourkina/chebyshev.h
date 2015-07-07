/* This file is automatically generated. DO NOT EDIT! */

#ifndef _chebyshev_h
#define _chebyshev_h


void chebcoef(const float *b, float *coef, int n);
/*< coefficient >*/


float chebeval(const float *coef, float x, int n);
/*< evaluation >*/


void chebder(float x1, float x2, const float *coef, float *cder, int ncol);
/*< derivative >*/


void spline(const float *x, const float *b, int n, float yp1,float ypn, float *b2);
/*< spline coefficients >*/


float splineval(const float *x, const float *b, const float *b2, int n,float xstar);
/*< spline evaluation >*/

#endif
