/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_convolution_h
#define _sf_convolution_h


void convolve_cwp (int lx, int ifx, float *x,
		   int ly, int ify, float *y,
		   int lz, int ifz, float *z);
/*<
****************************************************************************
Compute z = x convolved with y; i.e.,

ifx+lx-1
z[i] =   sum    x[j]*y[i-j]  ;  i = ifz,...,ifz+lz-1
j=ifx
******************************************************************************
Input:
lx		length of x array
ifx		sample index of first x
x		array[lx] to be convolved with y
ly		length of y array
ify		sample index of first y
y		array[ly] with which x is to be convolved
lz		length of z array
ifz		sample index of first z

Output:
z		array[lz] containing x convolved with y
******************************************************************************
Notes:
The x samples are contained in x[0], x[1], ..., x[lx-1]; likewise for
the y and z samples.  The sample indices of the first x, y, and z values
determine the location of the origin for each array.  For example, if
z is to be a weighted average of the nearest 5 samples of y, one might
use 
...
x[0] = x[1] = x[2] = x[3] = x[4] = 1.0/5.0;
conv(5,-2,x,lx,0,y,ly,0,z);
...
In this example, the filter x is symmetric, with index of first sample = -2.

This function is optimized for architectures that can simultaneously perform
a multiply, add, and one load from memory; e.g., the IBM RISC System/6000.
Because, for each value of i, it accumulates the convolution sum z[i] in a
scalar, this function is not likely to be optimal for vector architectures.
******************************************************************************
Author:  Dave Hale, Colorado School of Mines, 11/23/91
****************************************************************************>*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_intlin_h
#define _sf_intlin_h


void intlin (int nin /* length of xin and yin arrays */, 
	     const float *xin /* array[nin] of monotonically increasing or decreasing x values */, 
	     const float *yin /* array[nin] of input y(x) values */, 
	     float yinl /* value used to extraplate y(x) to left of input yin values */, 
	     float yinr /* value used to extraplate y(x) to right of input yin values */, 
	     int nout /* length of xout and yout arrays */, 
	     const float *xout /* array[nout] of x values at which to evaluate y(x) */, 
	     float *yout /* array[nout] of linearly interpolated y(x) values */);
/*< evaluate y(x) via linear interpolation of y(x[0]), y(x[1]), ...

Notes:
xin values must be monotonically increasing or decreasing.

Extrapolation of the function y(x) for xout values outside the range
spanned by the xin values in performed as follows:

	For monotonically increasing xin values,
		yout=yinl if xout<xin[0], and yout=yinr if xout>xin[nin-1].

	For monotonically decreasing xin values, 
		yout=yinl if xout>xin[0], and yout=yinr if xout<xin[nin-1].

        If nin==1, then the monotonically increasing case is used. >*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_intsinc8_h
#define _sf_intsinc8_h


#include <rsf.h>


void ints8c (int nxin         /* number of x values at which y(x) is input */, 
	     float dxin       /* x sampling interval for input y(x) */, 
	     float fxin       /* x value of first sample input */, 
	     sf_complex *yin  /* [nxin] array of input y(x) values:  yin[0] = y(fxin), etc. */,
	     sf_complex yinl  /* value used to extrapolate yin values to left of yin[0] */, 
	     sf_complex yinr  /* value used to extrapolate yin values to right of yin[nxin-1] */, 
	     int nxout        /* number of x values a which y(x) is output */, 
	     float *xout      /* [nxout] array of x values at which y(x) is output */, 
	     sf_complex *yout /* [nxout] array of output y(x):  yout[0] = y(xout[0]), etc. */);
/*< Interpolation of a uniformly-sampled complex function y(x) via a
table of 8-coefficient sinc approximations; maximum error for frequiencies
less than 0.6 nyquist is less than one percent.

Because extrapolation of the input function y(x) is defined by the
left and right values yinl and yinr, the xout values are not restricted
to lie within the range of sample locations defined by nxin, dxin, and
fxin. >*/


void ints8r (int nxin /* number of x values at which y(x) is input */, 
	     float dxin /* x sampling interval for input y(x) */, 
	     float fxin /* x value of first sample input */, 
	     float *yin /* [nxin] array of input y(x) values:  yin[0] = y(fxin), etc. */, 
	     float yinl  /* value used to extrapolate yin values to left of yin[0] */, 
	     float yinr  /* alue used to extrapolate yin values to right of yin[nxin-1] */, 
	     int nxout   /* number of x values a which y(x) is output */, 
	     float *xout /* [nxout] array of x values at which y(x) is output */, 
	     float *yout /* [nxout] array of output y(x):  yout[0] = y(xout[0]), etc. */);
/*< Interpolation of a uniformly-sampled real function y(x) via a
table of 8-coefficient sinc approximations; maximum error for frequiencies
less than 0.6 nyquist is less than one percent.

Because extrapolation of the input function y(x) is defined by the
left and right values yinl and yinr, the xout values are not restricted
to lie within the range of sample locations defined by nxin, dxin, and
fxin. >*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_inttable8_h
#define _sf_inttable8_h


void intt8c (int ntable       /* number of tabulated interpolation operators; ntable>=2 */, 
	     float table[][8] /* array of tabulated 8-point interpolation operators */,
	     int nxin         /* number of x values at which y(x) is input */, 
	     float dxin       /* x sampling interval for input y(x) */, 
	     float fxin       /* x value of first sample input */, 
	     sf_complex *yin  /* array of input y(x) values:  yin[0] = y(fxin), etc. */,
	     sf_complex yinl  /* value used to extrapolate yin values to left of yin[0] */, 
	     sf_complex yinr  /* value used to extrapolate yin values to right of yin[nxin-1] */, 
	     int nxout        /* number of x values at which y(x) is output */, 
	     float *xout      /* x values a which y(x) is output */, 
	     sf_complex *yout /* array of output y(x) values:  yout[0] = y(xout[0]), etc. */);
/*< interpolation of a uniformly-sampled complex function y(x)
  via a table of 8-coefficient interpolators 

  The table of interpolation operators must be as follows:

Let d be the distance, expressed as a fraction of dxin, from a particular
xout value to the sampled location xin just to the left of xout.  Then,
for d = 0.0,

table[0][0:7] = 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0

are the weights applied to the 8 input samples nearest xout.
Likewise, for d = 1.0,

table[ntable-1][0:7] = 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0

are the weights applied to the 8 input samples nearest xout.  In general,
for d = (float)itable/(float)(ntable-1), table[itable][0:7] are the
weights applied to the 8 input samples nearest xout.  If the actual sample
distance d does not exactly equal one of the values for which interpolators
are tabulated, then the interpolator corresponding to the nearest value of
d is used.

Because extrapolation of the input function y(x) is defined by the left
and right values yinl and yinr, the xout values are not restricted to lie
within the range of sample locations defined by nxin, dxin, and fxin. >*/


void intt8r (int ntable       /* number of tabulated interpolation operators; ntable>=2 */, 
	     float table[][8] /* array of tabulated 8-point interpolation operators */,
	     int nxin         /* number of x values at which y(x) is input */, 
	     float dxin       /* x sampling interval for input y(x) */, 
	     float fxin       /* x value of first sample input */, 
	     float *yin       /* array of input y(x) values:  yin[0] = y(fxin), etc. */,
	     float yinl       /* value used to extrapolate yin values to left of yin[0] */, 
	     float yinr       /* value used to extrapolate yin values to right of yin[nxin-1] */, 
	     int nxout        /* number of x values at which y(x) is output */, 
	     float *xout      /* x values at which y(x) is output */, 
	     float *yout      /* array of output y(x) values:  yout[0] = y(xout[0]), etc. */);
/*< interpolation of a uniformly-sampled complex function y(x)
  via a table of 8-coefficient interpolators 

  The table of interpolation operators must be as follows:

Let d be the distance, expressed as a fraction of dxin, from a particular
xout value to the sampled location xin just to the left of xout.  Then,
for d = 0.0,

table[0][0:7] = 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0

are the weights applied to the 8 input samples nearest xout.
Likewise, for d = 1.0,

table[ntable-1][0:7] = 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0

are the weights applied to the 8 input samples nearest xout.  In general,
for d = (float)itable/(float)(ntable-1), table[itable][0:7] are the
weights applied to the 8 input samples nearest xout.  If the actual sample
distance d does not exactly equal one of the values for which interpolators
are tabulated, then the interpolator corresponding to the nearest value of
d is used.

Because extrapolation of the input function y(x) is defined by the left
and right values yinl and yinr, the xout values are not restricted to lie
within the range of sample locations defined by nxin, dxin, and fxin. >*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_mksinc_h
#define _sf_mksinc_h


void mksinc (float d     /* fractional distance to interpolation point; 0.0<=d<=1.0 */, 
	     int lsinc   /* length of sinc approximation; lsinc%2==0 and lsinc<=20 */, 
	     float *sinc /* [lsinc] array containing interpolation coefficients */);
/*< Compute least-squares optimal sinc interpolation coefficients.

The coefficients are a least-squares-best approximation to the ideal
sinc function for frequencies from zero up to a computed maximum
frequency.  For a given interpolator length, lsinc, mksinc computes
the maximum frequency, fmax (expressed as a fraction of the nyquist
frequency), using the following empirically derived relation (from
a Western Geophysical Technical Memorandum by Ken Larner):

	fmax = min(0.066+0.265*log(lsinc),1.0)

Note that fmax increases as lsinc increases, up to a maximum of 1.0.
Use the coefficients to interpolate a uniformly-sampled function y(i) 
as follows:

            lsinc-1
    y(i+d) =  sum  sinc[j]*y(i+j+1-lsinc/2)
              j=0

Interpolation error is greatest for d=0.5, but for frequencies less
than fmax, the error should be less than 1.0 percent. >*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_sinc_h
#define _sf_sinc_h


float fsinc (float x);
/*< Return sinc(x) = sin(PI*x)/(PI*x) (float version) >*/


double dsinc (double x);
/*< Return sinc(x) = sin(PI*x)/(PI*x) (double version) >*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_toeplitz_h
#define _sf_toeplitz_h


void toeplitz (int n           /* matrix size */,
	       const double *r /* [n] top row of the matrix */, 
	       double *f       /* [n] inverted in place */,
	       double *a       /* [n] work array */);
/*< apply the solver >*/


void stoepf (int n, float r[], float g[], float f[], float a[]);
/*<
****************************************************************************
Solve a symmetric Toeplitz linear system of equations Rf=g for f
(float version) 
******************************************************************************
Input:
n		dimension of system
r		array[n] of top row of Toeplitz matrix
g		array[n] of right-hand-side column vector

Output:
f		array[n] of solution (left-hand-side) column vector
a		array[n] of solution to Ra=v (Claerbout, FGDP, p. 57)
******************************************************************************
Notes:
This routine does NOT solve the case when the main diagonal is zero, it
just silently returns.

The left column of the Toeplitz matrix is assumed to be equal to the top
row (as specified in r); i.e., the Toeplitz matrix is assumed symmetric.
******************************************************************************
Author:  Dave Hale, Colorado School of Mines, 06/02/89
****************************************************************************>*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_xcor_h
#define _sf_xcor_h


void xcor (int lx, int ifx, float *x,
	   int ly, int ify, float *y, 
	   int lz, int ifz, float *z);
/*<
****************************************************************************
Compute z = x cross-correlated with y; i.e.,

           ifx+lx-1
    z[i] =   sum    x[j]*y[i+j]  ;  i = ifz,...,ifz+lz-1
            j=ifx
******************************************************************************
Input:
lx		length of x array
ifx		sample index of first x
x		array[lx] to be cross-correlated with y
ly		length of y array
ify		sample index of first y
y		array[ly] with which x is to be cross-correlated
lz		length of z array
ifz		sample index of first z

Output:
z		array[lz] containing x cross-correlated with y
******************************************************************************
Notes:
See notes for convolution function convolve_cwp().
This function performs cross-correlation by
(1) reversing the samples in the x array while copying
    them to a temporary array, and
(2) calling function convolve_cwp() with ifx set to 1-ifx-lx.
Assuming that the overhead of reversing the samples in x is negligible,
this method enables cross-correlation to be performed as efficiently as
convolution, while reducing the amount of code that must be optimized
and maintained.
******************************************************************************
Author:  Dave Hale, Colorado School of Mines, 11/23/91
****************************************************************************>*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_yxtoxy_h
#define _sf_yxtoxy_h


void yxtoxy (int nx /* number of samples of y(x) */, 
	     float dx /* x sampling interval; dx>0.0 is required */, 
	     float fx /* first x */, 
	     const float *y /* array[nx] of y(x) values; y[0] < y[1] < ... < y[nx-1] required */, 
	     int ny /* number of samples of x(y) */, 
	     float dy /* y sampling interval; dy>0.0 is required */, 
	     float fy /* first y */, 
	     float xylo /* x value assigned to x(y) when y is less than smallest y(x) */, 
	     float xyhi /* x value assigned to x(y) when y is greater than largest y(x) */, 
	     float *x /* array[ny] of x(y) values */);
/*< Compute a regularly-sampled, monotonically increasing function x(y)
from a regularly-sampled, monotonically increasing function y(x) by
inverse linear interpolation.
***
Notes:
User must ensure that:
(1) dx>0.0 && dy>0.0
(2) y[0] < y[1] < ... < y[nx-1] >*/

#endif
/* This file is automatically generated. DO NOT EDIT! */

#ifndef _sf_xindex_h
#define _sf_xindex_h


void xindex (int nx /* number of x values in array ax */,
	     const float *ax /* array[nx] of monotonically increasing or decreasing x values */, 
	     float x /* the value for which index is to be determined */, 
	     int *index /* index determined previously (used to begin search) */);
/*< Determine index of x with respect to an array of x values

Output:
index		for monotonically increasing ax values, the largest index
		for which ax[index]<=x, except index=0 if ax[0]>x;
		for monotonically decreasing ax values, the largest index
		for which ax[index]>=x, except index=0 if ax[0]<x
******************************************************************************
Notes:
This function is designed to be particularly efficient when called
repeatedly for slightly changing x values; in such cases, the index 
returned from one call should be used in the next. >*/

#endif
